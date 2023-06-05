def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        T, D = map(int, input().split())
        sushi.append((T, D))
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    kind = set()
    delicious = 0
    for i in range(K):
        kind.add(sushi[i][0])
        delicious += sushi[i][1]
    # print(kind, delicious)
    ans = delicious + len(kind) ** 2
    # print(ans)
    kind = list(kind)
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        else:
            kind.append(sushi[i][0])
            delicious += sushi[i][1] - sushi[K - 1][1]
            ans = max(ans, delicious + len(kind) ** 2)
    print(ans)

if __name__ == '__main__':
    main()