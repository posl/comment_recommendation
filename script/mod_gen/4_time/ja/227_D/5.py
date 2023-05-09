def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for a in A[:K]:
        ans += a
    print(ans)

if __name__ == '__main__':
    solve()