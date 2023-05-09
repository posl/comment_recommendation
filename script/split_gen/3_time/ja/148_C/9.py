def solve():
    a,b = map(int,input().split())
    x = a*b
    for i in range(1,100000):
        if i*a%b==0:
            print(i*a)
            return
        if i*b%a==0:
            print(i*b)
            return
    print(x)
