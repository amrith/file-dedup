import json
import sys
import utils

def main(argv):
    hashes = {}

    with open(argv[1], 'r') as f:
        hashes = json.load(f)

    # dups is the set of duplicate hashes
    dups = [k for k,v in hashes.iteritems() if len(v) > 1]
    
    duplist = []

    for d in dups:
        duplist.append(hashes[d])

    sorted(duplist, key=lambda x: sorted(x)[0])

    for e in duplist:
        print "Possible duplicate files:"
        for f in e:
            print "\t" + f
        print "\n"

if __name__ == "__main__":
    main(sys.argv)
