def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append([t, d])
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    # 種類数を数える
    kind = set()
    for i in range(K):
        kind.add(sushi[i][0])
    #print(kind)
    # 種類数とおいしさの合計を計算
    ans = 0
    for i in range(K):
        ans += sushi[i][1]
    ans += len(kind) ** 2
    #print(ans)
    # おいしい寿司から順に種類数を増やしていく
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        kind.add(sushi[i][0])
        #print(kind)
        tmp = ans
        tmp -= sushi[i-K][1]
        tmp += sushi[i][1]
        tmp += 2 * len(kind) - 1
        ans = max(ans, tmp)
        #print(ans)
    print(ans)
