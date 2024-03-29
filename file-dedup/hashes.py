#
# a simple utility to find duplicated files
#
# Amrith
#

import argparse
import sys
import json
import utils

def compute(path):
    hashes = utils.compute_hashes(path)

    json.dump(hashes, sys.stdout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute file hashes.')
    parser.add_argument('path', metavar='p', help='the path to examine')
    args = parser.parse_args()

    if args.path:
        compute(args.path)
