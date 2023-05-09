def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a + [n + 1]
    b = []
    for i in range(m + 1):
        b.append(a[i + 1] - a[i] - 1)
    k = min(b)
    ans = 0
    for i in range(m + 1):
        ans += (b[i] - 1) // k + 1
    print(ans)
