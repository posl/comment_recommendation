def solve(n):
    if n==0:
        return 0
    a=0
    b=0
    while True:
        a3=a**3
        if a3>n:
            break
        b=0
        while True:
            b3=b**3
            if a3+a**2*b+a*b**2+b3>n:
                break
            if a3+a**2*b+a*b**2+b3==n:
                return a**3+a**2*b+a*b**2+b3
            b+=1
        a+=1
    return -1
n=int(input())
print(solve(n))
