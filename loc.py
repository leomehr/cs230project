#!/usr/bin/env python

from json import load
from sys import argv

def loc(nb):
    cells = load(open(nb))['cells']
    return sum(len(c['source']) for c in cells if c['cell_type'] == 'code')

def run(ipynb_files):
    for f in ipynb_files:
        print(loc(f), ' ', f)
    print('total: ', sum(loc(nb) for nb in ipynb_files))

if __name__ == '__main__':
    run(argv[1:])

