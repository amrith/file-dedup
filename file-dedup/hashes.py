#
# a simple utility to find duplicated files
#
# Amrith
#

import sys
import json
import utils

def compute(argv, duplicates_only=True):
    hashes = utils.compute_hashes(argv[1])

    if duplicates_only:
        dups = [k for k,v in hashes.iteritems() if len(v) > 1]
    
        dupdict = {}

        for d in dups:
            dupdict[d] = hashes[d]

        json.dump(dupdict, sys.stdout)
    else:
        json.dump(hashes, sys.stdout)

if __name__ == "__main__":
    compute(sys.argv)
