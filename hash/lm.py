from passlib.hash import lmhash
import sys

password = sys.argv[1]
lm_hash = lmhash.hash(password)
print(lm_hash)
