def solve():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        p = 1
        while i<K:
            i *= 2
            p /= 2
        ans += p
    print(ans/N)

if __name__ == '__main__':
    solve()