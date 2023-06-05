def main():
    n = int(input())
    t = [0] * (n+1)
    k = [0] * (n+1)
    a = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        t[i], k[i], *a[i] = map(int, input().split())
    ans = 0
    for i in range(n, 0, -1):
        ans = max(ans, t[i] + max([t[j] for j in a[i]]))
    print(ans)
