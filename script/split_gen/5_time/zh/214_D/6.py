def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[2])
    cnt = [1] * n
    ans = 0
    for u, v, w in edges:
        ans += w * cnt[u-1] * cnt[v-1]
        cnt[u-1] += cnt[v-1]
    print(ans)
