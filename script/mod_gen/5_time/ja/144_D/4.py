def solve():
    a,b,x = map(int,input().split())
    if x > a*a*b/2:
        print(90 - 2*(a*a*b-x)/a/a/a)
    else:
        print(2*x/b/a/b)

if __name__ == '__main__':
    solve()