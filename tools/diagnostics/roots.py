#!/usr/bin/env python3

"""
Checks whether the uniqueness of root is violated. Writes violation to log

Usage
    roots.py <path-to-input>

"""

import argparse
import os
from glob import glob
import pyconll
import logging

parser = argparse.ArgumentParser()
parser.add_argument("path_to_input", help="path to input; might be a file or a dir")
parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.INFO)
    logging.info("Verbose output activated")

if os.path.isfile(args.path_to_input):
    infs = [args.path_to_input]
elif os.path.isdr(args.path_to_input):
    infs = glob(os.path.join(args.path_to_input, "*.conllu"))
else:
    infs = []
    
for f in infs:
    fbasename = os.path.basename(f)
    c = pyconll.iter_from_file(f)
    for sent in c:
        sentid = sent.id
        roots = [n for n in sent if n.head == '0']
        if len(roots) == 0:
            logging.error(f"No root found for sent: {fbasename}, {sentid}")
        elif len(roots) > 1:
            logging.error(f'More than 1 root found for sent: {fbasename}, {sentid}')
        else:
            logging.info(f'No problem with sent: {fbasename}, {sentid}')
        
            
