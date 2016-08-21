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
    hashes = utils.duplicate_hashes(path)

    for k,v in hashes.iteritems():
        print "Possibly duplicate files"
        names = []
        for e in v:
            names.append(e['name'])

        sn = sorted(names)
        for n in sn:
            print "\t%s" % n

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute file hashes.')
    parser.add_argument('path', metavar='p', help='the path to examine')
    args = parser.parse_args()

    if args.path:
        compute(args.path)
