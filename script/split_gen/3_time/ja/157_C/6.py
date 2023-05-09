def main():
    n,m = map(int,input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i],c[i] = map(int,input().split())
    if m == 0:
        if n == 1:
            print(0)
        else:
            print(10**(n-1))
    else:
        if n == 1:
            if s[0] == 1:
                print(c[0])
            else:
                print(-1)
        else:
            if s[0] == 1:
                if c[0] == 0:
                    print(-1)
                else:
                    for i in range(n-1):
                        print(c[0],end="")
                    for i in range(m-1):
                        print(c[i+1],end="")
                    print()
            else:
                for i in range(n):
                    print(1,end="")
                for i in range(m):
                    print(c[i],end="")
                print()
