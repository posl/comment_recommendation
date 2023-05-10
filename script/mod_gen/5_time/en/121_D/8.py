def xor(a,b):
    if a == b:
        return a
    elif a < b:
        return xor(a,b-1)^b
    else:
        return xor(a,b+1)^b
A,B = [int(x) for x in input().split()]
print(xor(A,B))

if __name__ == '__main__':
    xor()