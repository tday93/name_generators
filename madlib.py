import random as rand
# own modules
from grimoire import jsonutils as ju


def main(schema):
    output = ""
    pat = schema["pattern"]
    for item in pat:
        if item.startswith("!"):
            piece = rand.choice(schema[item[1:]])
            output = output + piece
        else:
            output = output + piece
    return output


if __name__ == "__main__":
    schema = ju.read_json("fantasy_village.json")
    out = main(schema)
    print(out)
