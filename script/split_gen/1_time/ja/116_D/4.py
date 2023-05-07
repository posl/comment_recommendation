def main():
    N, K = map(int, input().split())
    sushi = [tuple(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    kind = set()
    point = 0
    for i in range(K):
        kind.add(sushi[i][0])
        point += sushi[i][1]
    ans = point + len(kind) ** 2
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        kind.add(sushi[i][0])
        point += sushi[i][1]
        point -= sushi[i-K][1]
        ans = max(ans, point + len(kind) ** 2)
    print(ans)
