def main():
    a,b,k = map(int,input().split())
    if a >= k:
        a = a - k
    else:
        b = b - (k - a)
        a = 0
        if b < 0:
            b = 0
    print(a,b)
