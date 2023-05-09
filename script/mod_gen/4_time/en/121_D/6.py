def xor(a,b):
    if a == b:
        return a
    elif a%2 == 0:
        return xor(a+1,b)^a
    else:
        return xor(a+1,b)
a,b = map(int,input().split())
print(xor(a,b))

if __name__ == '__main__':
    xor()