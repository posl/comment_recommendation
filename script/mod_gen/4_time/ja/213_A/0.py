def xor(a,b):
    c = 0
    for i in range(8):
        if a%2 != b%2:
            c += 2**i
        a = a//2
        b = b//2
    return c
a,b = map(int,input().split())
print(xor(a,b))

if __name__ == '__main__':
    xor()