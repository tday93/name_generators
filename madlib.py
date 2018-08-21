#!/usr/local/bin/python3
import sys
import random as rand
from os.path import join, split
# own modules
from grimoire import jsonutils as ju

"""
Madlibbing module. Builds strings out of defined patterns.

Command line takes 2 arguments

1. path of the base schema
2. the desired number of items to generate

Note that all referenced schema must be in the same directory

"""


class Madlib():

    def __init__(self, base_file, directory):
        self.base_file = base_file
        self.directory = directory
        self.schema, self.pattern = self.load_schema(self.base_file)

    def generate(self, n):
        output = []
        while len(output) < n:
            item = self.unpack_pattern(self.pattern, self.schema)
            if item not in output:
                output.append(item)
        return output

    def unpack_pattern(self, pattern, schema):
        output = ""
        pat_list = pattern.split(" ")
        for pat in pat_list:
            inst, tag = pat.split("#")
            # shortcut if plaintext
            if "$" in inst:
                tag_out = tag.replace("_", " ")
                output = output + tag_out
                continue
            # load external schema
            if "&" in inst:
                sub_schema, sub_pattern = self.load_schema(tag)
                result = self.unpack_pattern(sub_pattern, sub_schema)
            # unpack tag if not external schema or plaintext
            else:
                corpus = schema[tag]
                if isinstance(corpus, str):
                    tag_out = corpus
                else:
                    tag_out = rand.choice(corpus)

            # recurse if reference to subpattern
            if "!" in inst:
                result = self.unpack_pattern(tag_out, schema)
            # dont if not
            elif "*" in inst:
                result = tag_out

            # simple instructions
            if "^" in inst:
                result = result.capitalize()
            if "+" in inst:
                result = result.upper()
            if "-" in inst:
                result = result.lower()
            output = output + result
        return output

    def load_schema(self, filename):
        file_path = join(self.directory, filename)
        schema = ju.read_json(file_path)
        pattern = schema["pattern"]
        return schema, pattern


if __name__ == "__main__":
    file_path = sys.argv[1]
    directory, filename = split(file_path)
    n = int(sys.argv[2])
    m = Madlib(filename, directory)
    out = m.generate(n)
    for item in out:
        print(item)
