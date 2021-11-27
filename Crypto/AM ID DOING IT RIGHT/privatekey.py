from Crypto.Util.number import *
f = open("chall.enc", "rb")
ans = bytes_to_long(f.read())
print(ans)