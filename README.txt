A simple file deduplication utility

Will identify files that are potentially duplicates of each other.

This also includes the file-dedup library which can be used by itself.

     from file_dedup.utils import compute_hashes

     hashes = compute_hashes(path)

hashes is a dictionary that looks like:

       { 'hashvalue1': [
         { 'name': name, 'size': size },
           ... ],
         'hashvalue2': [...]
       }

In other words, for each hash (key), the value is a list of
disctionaries where each element is has a name and a size.
{
   "62779c8df215502849dce5f6d8321caa": [
      {"name": "/tmp/utils.pyc", "size": 1899}],
   "3f04e1bcf72988422be91bf9d2791aea": [
      {"name": "/tmp/dups.py", "size": 526},
      {"name": "/tmp/dups2.py", "size": 526}],
   "5cba436660471bf7a9de6fe412b29e64": [
      {"name": "/tmp/utils.py", "size": 1235}],
   "3ec03444b4db80ef14f5448f19731858": [
      {"name": "/tmp/hashes.py", "size": 493}]
}

An example (hashes.py) is provided which illustrates this.

To only retreive those files which are duplicates

     from file_dedup.utils import duplicates_hashes

     hashes = duplicates_hashes(path)

An example (duplicates.py) is provided which illustrates this.
