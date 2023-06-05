def solve():
    N = int(input())
    ds = list(map(int,input().split()))
    ds.sort()
    ans = 0
    for i in range(N//2):
        if ds[i] != ds[i+N//2]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()