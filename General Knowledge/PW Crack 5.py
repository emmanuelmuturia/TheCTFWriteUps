# picoCTF{h45h_sl1ng1ng_36e992a6}

# Run the following to get the correct password:

#!/usr/bin/env python3


import hashlib

goodRead = open('dictionary.txt','r')
correct_pw_hash = open('level5.hash.bin', 'rb').read()

myList = []

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


for items in goodRead:
    myList.append(items.strip(' \n'))

for newItems in myList:
    if hash_pw(newItems) == correct_pw_hash:
        print(newItems)
        break
