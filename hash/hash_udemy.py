# ! Hashing is reversible

import hashlib

hashval = input("[*] Enter a string to hash: ")

hash_obj1 = hashlib.md5() #treat as a hash function # Note: md5 - 128-bit hash value
hash_obj1.update(hashval.encode()) #encodes the input text string into byte 
print("MD5 hash value: " + hash_obj1.hexdigest()) #hexdigest - Return the digest of the data passed to the update()

hash_obj2 = hashlib.sha1() # Note: sha1 - 160-bit hash value
hash_obj2.update(hashval.encode())
print("SHA1 hash value: " + hash_obj2.hexdigest())

hash_obj3 = hashlib.sha224() # Note: sha224 - 224-bit hash value
hash_obj3.update(hashval.encode())
print("SHA224 hash value: " + hash_obj3.hexdigest())

hash_obj4 = hashlib.sha256() # Note: sha256 - 256-bit hash value
hash_obj4.update(hashval.encode())
print("SHA256 hash value: " + hash_obj4.hexdigest())

hash_obj5 = hashlib.sha512() # Note: sha512 - 512-bit hash value
hash_obj5.update(hashval.encode())
print("SHA512 hash value: " + hash_obj5.hexdigest())
