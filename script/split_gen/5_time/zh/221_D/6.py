def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    for i in range(n):
        a[i] -= 1
    d = [0] * (2 * 10**9 + 2)
    for i in range(n):
        d[a[i]] += 1
        d[a[i] + b[i]] -= 1
    for i in range(1, 2 * 10**9 + 2):
        d[i] += d[i - 1]
    e = [0] * (n + 1)
    for i in range(2 * 10**9 + 1):
        if d[i] > 0:
            e[d[i]] += 1
    for i in range(1, n + 1):
        print(e[i], end=" ")
    print()
