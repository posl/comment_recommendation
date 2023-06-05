def solve():
    a,b=map(int,input().split())
    print((a+1)/2+((a+1)**2/4+b)**0.5)

if __name__ == '__main__':
    solve()