def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    ans = 0
    for i in range(n):
        good = True
        for j in adj[i]:
            if h[i] <= h[j]:
                good = False
                break
        if good:
            ans += 1
    print(ans)
