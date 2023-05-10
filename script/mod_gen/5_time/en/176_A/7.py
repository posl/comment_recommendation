def solve():
    N,X,T = map(int, input().split())
    print((N//X + (N%X!=0))*T)

if __name__ == '__main__':
    solve()