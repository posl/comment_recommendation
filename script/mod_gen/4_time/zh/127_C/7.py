def solve():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        l[a - 1] += 1
        l[b] -= 1
    for i in range(n):
        l[i + 1] += l[i]
    print(l.count(m))

if __name__ == '__main__':
    solve()