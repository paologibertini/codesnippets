#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description="Extends logfile with field names")
parser.add_argument("inputfile", nargs="?", type=argparse.FileType("r"), help="Input file (default: stdin)", default=sys.stdin)
parser.add_argument("-sep", dest="delimiter", help="Separator", default="|")
parser.add_argument("-desc", dest="desc", help="Field list file", default=None)
parser.add_argument("-iln", dest="iln", help="Show line numbers (input)", action="store_true")
parser.add_argument("-oln", dest="oln", help="Show line numbers (output)", action="store_true")
parser.add_argument("-grep", dest="grep", help="filter input record", default=None)
args = parser.parse_args()

# can be only input or output line numbers
if args.iln:
    args.oln = False

campi = []
if args.desc is not None:
    with open(args.desc, "r") as f:
        campi = f.read().splitlines()

i = 1

for line in args.inputfile:
    if not campi:
        # first line contains field names
        campi = line[:-1].split(args.delimiter)
        print(f"{campi=}")
        i += 1 if args.iln else 0
        continue

    if args.grep is not None and args.grep not in line:
        i += 1 if args.iln else 0
        continue
    output = [f"{k}={v}" for k, v in zip(campi, line.split(args.delimiter))]
    if args.iln or args.oln:
        sys.stdout.write(f"{i}: ")
        i += 1
    sys.stdout.write(" | ".join(output))
