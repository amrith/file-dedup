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
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

def makepath(root, name):
    return os.path.abspath(os.path.expanduser(root + os.sep + name))

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

            e = { 'name': path, 'size': s }
            if m in hashes.keys():
                hashes[m].append(e)
            else:
                hashes[m] = [e]

    return hashes

def duplicate_hashes(top=os.sep):
    h = compute_hashes(top)
    dups = {}

    for k, v in h.iteritems():
        if len(v) > 1:
            dups[k] = v

    return dups
