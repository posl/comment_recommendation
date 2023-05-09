def solve():
    n,x,t = map(int,input().split())
    a = n // x
    b = n % x
    if b != 0:
        a += 1
    print(a * t)
