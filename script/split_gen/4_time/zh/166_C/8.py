def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]
    # 良い天気台の数
    ans = n
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for a, b in ab:
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    for i in range(n):
        for j in adj[i]:
            if h[i] <= h[j]:
                ans -= 1
                break
    print(ans)
