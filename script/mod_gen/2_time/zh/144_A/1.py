def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ok = j
            ng = N
            while abs(ok-ng) > 1:
                mid = (ok+ng)//2
                if L[mid] < L[i]+L[j]:
                    ok = mid
                else:
                    ng = mid
            ans += ok-j
    print(ans)

if __name__ == '__main__':
    solve()