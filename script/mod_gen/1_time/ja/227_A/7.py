def solve():
    n,k,a = map(int,input().split())
    print((a+k-2)%n+1)
solve()

if __name__ == '__main__':
    solve()