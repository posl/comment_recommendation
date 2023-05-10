def solve():
    #import sys
    #input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n):
        if i < k:
            continue
        ans += a[i]
    print(ans)
    return 0

if __name__ == '__main__':
    solve()