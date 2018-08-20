#!/usr/local/bin/python3
import sys
import random as rand
# own modules
from grimoire import jsonutils as ju


def main(filename, n):
    schema, pattern = load_schema(filename)
    for i in range(n):
        output = unpack_pattern(pattern, schema)
        print(output)


def unpack_pattern(pattern, schema):
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
            sub_schema, sub_pattern = load_schema(tag)
            result = unpack_pattern(sub_pattern, sub_schema)
        # unpack tag if not external schema or plaintext
        else:
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


def load_schema(filename):
    schema = ju.read_json(filename)
    pattern = schema["pattern"]
    return schema, pattern


if __name__ == "__main__":
    filename = sys.argv[1]
    n = int(sys.argv[2])
    main(filename, n)
