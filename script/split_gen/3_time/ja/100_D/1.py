def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] if i >> k & 1 else -cake[j][k] for k in range(3)]))
        tmp.sort()
        ans = max(ans, sum(tmp[-M:]))
    print(ans)
