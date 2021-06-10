


key = []
for x in range(256):
    if(int("13",16) ^ x == ord("H")):
        key.append(x)
        break
for x in range(256):
    if(int("4a",16) ^ x == ord("T")):
        key.append(x)
        break
for x in range(256):
    if(int("f6",16) ^ x == ord("B")):
        key.append(x)
        break
for x in range(256):
    if(int("e1",16) ^ x == ord("{")):
        key.append(x)
        break
flag = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'
arr = []
for n in range(len(flag)):
    if(n%2==0):
        mr = int(flag[n]+flag[n+1],16)
        arr.append(mr)
xored = b""
for i in range(len(arr)):
    xored += bytes([arr[i] ^ key[i % 4]])

print(xored)












