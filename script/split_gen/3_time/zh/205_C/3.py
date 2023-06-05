def pow(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result
a,b,c = map(int,input().split())
