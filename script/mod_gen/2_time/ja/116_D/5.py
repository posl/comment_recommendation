def main():
    N, K = map(int, input().split())
    Sushi = []
    for i in range(N):
        t_i, d_i = map(int, input().split())
        Sushi.append([t_i, d_i])
    Sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    kind.add(Sushi[0][0])
    point = Sushi[0][1]
    for i in range(1, K):
        if Sushi[i][0] in kind:
            point += Sushi[i][1]
        else:
            kind.add(Sushi[i][0])
            point += Sushi[i][1] + len(kind) ** 2 - (len(kind) - 1) ** 2
    ans = point
    for i in range(K, N):
        if len(kind) == K:
            break
        if Sushi[i][0] in kind:
            continue
        point += Sushi[i][1] - Sushi[K - 1][1]
        point += len(kind) ** 2 - (len(kind) - 1) ** 2
        kind.add(Sushi[i][0])
        ans = max(ans, point)
    print(ans)

if __name__ == '__main__':
    main()