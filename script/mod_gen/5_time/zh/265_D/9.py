def solve():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    min_a = [a[0]]
    max_a = [a[0]]
    for i in range(1, n):
        min_a.append(min(min_a[i - 1], a[i]))
        max_a.append(max(max_a[i - 1], a[i]))
    ans = 0
    for i in range(n):
        if min_a[i] >= p and max_a[i] <= r:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()