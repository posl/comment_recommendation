def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = -float('inf')
    for i in range(2 ** 3):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] * ((i >> k) & 1) * 2 - 1 for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)
