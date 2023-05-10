def xor(a,b):
    #print("a: " + str(a) + " b: " + str(b))
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a == 1:
        if b == 2:
            return 3
        if b == 3:
            return 2
    if a == 2:
        if b == 1:
            return 3
        if b == 3:
            return 1
    if a == 3:
        if b == 1:
            return 2
        if b == 2:
            return 1
    if a % 2 == 0:
        if b % 2 == 0:
            return xor(a//2,b//2) * 2
        else:
            return xor(a//2,b//2) * 2 + 1
    else:
        if b % 2 == 0:
            return xor(a//2,b//2) * 2 + 1
        else:
            return xor(a//2,b//2) * 2
a,b = map(int,input().split())
print(xor(a,b))
