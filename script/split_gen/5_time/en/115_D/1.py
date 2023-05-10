def main():
    n,x = map(int,input().split())
    p = [1]
    b = [1]
    for i in range(n):
        p.append(p[i]*2+1)
        b.append(b[i]*2+3)
    def f(n,x):
        if n == 0:
            return 1
        elif x == 1:
            return 0
        elif x <= 1+b[n-1]:
            return f(n-1,x-1)
        elif x == 2+b[n-1]:
            return p[n-1]+1
        elif x <= 2+2*b[n-1]:
            return p[n-1]+1+f(n-1,x-2-b[n-1])
        else:
            return 2*p[n-1]+1
    print(f(n,x))
