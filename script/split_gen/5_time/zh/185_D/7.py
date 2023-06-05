def main():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        a.append(0)
    a.append(n+1)
    a.sort()
    b = []
    for i in range(1, m+2):
        if a[i] - a[i-1] - 1 > 0:
            b.append(a[i] - a[i-1] - 1)
    k = min(b)
    ans = 0
    for i in range(len(b)):
        ans += (b[i] + k - 1) // k
    print(ans)
