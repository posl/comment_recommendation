def solve():
    import sys
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        ans = n - bisect.bisect_left(a, x)
        print(ans)

if __name__ == '__main__':
    solve()