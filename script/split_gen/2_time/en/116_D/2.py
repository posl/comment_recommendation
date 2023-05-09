def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    kinds = set()
    total = 0
    for i in range(K):
        kinds.add(sushi[i][0])
        total += sushi[i][1]
    ans = len(kinds) ** 2 + total
    for i in range(K, N):
        if sushi[i][0] in kinds:
            continue
        kinds.add(sushi[i][0])
        total += sushi[i][1]
        for j in range(K):
            if sushi[j][0] in kinds:
                continue
            kinds.remove(sushi[j][0])
            total -= sushi[j][1]
            break
        ans = max(ans, len(kinds) ** 2 + total)
    print(ans)
