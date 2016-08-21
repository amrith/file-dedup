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
        names = []
        for e in v:
            names.append(e['name'])

        sn = sorted(names)
        print "# Possibly duplicate files of %s" % sn[0]

        for n in sn[1:]:
            print "rm %s" % n

        print ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute file hashes.')
    parser.add_argument('path', metavar='p', help='the path to examine')
    args = parser.parse_args()

    if args.path:
        compute(args.path)
