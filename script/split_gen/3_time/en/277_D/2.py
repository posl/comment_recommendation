def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    b = [a[0]]
    for i in range(1, n+1):
        if a[i] == a[i-1]:
            continue
        b.append(a[i])
    n = len(b)
    c = [0] * n
    for i in range(n):
        c[i] = b[i] - b[i-1] - 1
    ans = 0
    for i in range(n):
        ans += (c[i] + 1) // 2
    print(ans)
