#!/usr/local/bin/python3
import sys
from grimoire import jsonutils as ju


def get_input(f, key):
    corpus = f[key]
    end = False
    while not end:
        item = input("Next Item: ")
        if item in corpus:
            print(f'"{item}" already in list {key}')
            continue
        elif item in ["q", "quit", "Quit", "exit", "Exit"]:
            end = True
            continue
        else:
            corpus.append(item)
    return f


if __name__ == "__main__":
    args = sys.argv
    filename = args[1]
    key = args[2]
    f = ju.read_json(filename)
    new_f = get_input(f, key)
    ju.write_json(filename, new_f)
