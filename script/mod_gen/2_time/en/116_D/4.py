def main():
    N, K = map(int, input().split())
    Sushi = [list(map(int, input().split())) for _ in range(N)]
    Sushi.sort(key=lambda x: x[1], reverse=True)
    s = 0
    variety = set()
    for i in range(K):
        s += Sushi[i][1]
        variety.add(Sushi[i][0])
    ans = s + len(variety) * len(variety)
    for i in range(K, N):
        if Sushi[i][0] in variety:
            continue
        else:
            variety.add(Sushi[i][0])
            for j in range(K):
                if Sushi[j][0] not in variety:
                    s = s - Sushi[j][1] + Sushi[i][1]
                    ans = max(ans, s + len(variety) * len(variety))
                    break
    print(ans)

if __name__ == '__main__':
    main()