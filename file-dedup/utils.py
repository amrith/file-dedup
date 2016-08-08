#
# a simple utility to find duplicated files
#
# Amrith
#

import os
import sys
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    sys.stderr.write('.')
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

def makepath(root, name):
    return root + os.sep + name

# compute_hashes
#
# returns a dictionary that looks like:
#
# { 'hashvalue1': [
#        { 'name': name, 'size': size },
#        ... ],
#   'hashvalue2': [
# ...]
#

def compute_hashes(top=os.sep):
    hashes = {}
    for root, dirs, files in os.walk(top):
	for f in files:
            path = makepath(root, f)
            m = md5(path)
            s = os.path.getsize(path)

            if m in hashes.keys():
                sys.stderr.write('+')
                hashes[m].append(path)
            else:
                hashes[m] = [path]

    return hashes

def main(argv):
    hashes = compute_hashes(argv[1])

    dups = [k for k,v in hashes.iteritems() if len(v) > 1]
    for d in dups:
        print "Possible duplicate files"
        for f in hashes[d]:
            print "\t" + f

        print "\n"

if __name__ == "__main__":
    main(sys.argv)
