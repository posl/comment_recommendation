def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = [0] * (n + 1)
    for i in range(n):
        d[c[i]] += 1
    e = [0] * (n + 1)
    for i in range(1, n + 1):
        e[b[c[i - 1] - 1]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += d[a[i - 1]] * e[i]
    print(ans)
