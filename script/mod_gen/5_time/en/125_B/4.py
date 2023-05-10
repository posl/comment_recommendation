def solve():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        diff = v[i] - c[i]
        if diff > 0:
            ans += diff
    print(ans)

if __name__ == '__main__':
    solve()