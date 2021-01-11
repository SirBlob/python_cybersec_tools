import hashlib

hashval = input("[*] Enter a string to hash: ").encode()

hashFunc = ["md5", "sha1", "sha224", "sha256", "sha512"]

for x in range(len(hashFunc)):
    hash_obj = getattr(hashlib, hashFunc[x])(hashval).hexdigest() 
    print(f"{hashFunc[x]} hash value: " + hash_obj)
