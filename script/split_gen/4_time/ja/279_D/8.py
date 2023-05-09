def solve():
    a,b = map(int,input().split())
    if a >= b:
        print(a)
        return
    else:
        print(a + b/2)
