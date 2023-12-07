from passlib.hash import nthash
import sys

password = sys.argv[1]
nt_hash = nthash.hash(password)
print(nt_hash)
