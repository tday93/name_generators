#!/usr/local/bin/python3
import sys
import random as rand
# own modules
from grimoire import jsonutils as ju


def main(schema):
    pattern = schema["pattern"]
    output = unpack_pattern(pattern, schema)
    return output


def unpack_pattern(pattern, schema):
    output = ""
    pat_list = pattern.split(" ")
    for pat in pat_list:
        inst, tag = pat.split("#")
        if "$" in inst:
            output = output + tag
            continue
        corpus = schema[tag]
        if isinstance(corpus, str):
            tag_out = corpus
        else:
            tag_out = rand.choice(corpus)
        # recurse if reference to subpattern
        if "!" in inst:
            result = unpack_pattern(tag_out, schema)
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


if __name__ == "__main__":
    filename = sys.argv[1]
    n = int(sys.argv[2])
    schema = ju.read_json(filename)
    for i in range(n):
        print(main(schema))
