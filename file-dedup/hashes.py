#
# a simple utility to find duplicated files
#
# Amrith
#

import sys
import json
import utils

def main(argv):
    hashes = utils.compute_hashes(argv[1])

    json.dump(hashes, sys.stdout)

if __name__ == "__main__":
    main(sys.argv)
