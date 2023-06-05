def xor(a,b):
    c = a^b
    return c
a,b = input().split()
a = int(a)
b = int(b)
c = xor(a,b)
print(c)
