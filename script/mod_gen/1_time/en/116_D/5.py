def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    kind = set()
    for i in range(K):
        kind.add(sushi[i][0])
        ans += sushi[i][1]
    ans += len(kind) ** 2
    for i in range(K, N):
        if sushi[i][0] in kind:
            continue
        kind.add(sushi[i][0])
        for j in range(K):
            if sushi[j][0] not in kind:
                continue
            kind.remove(sushi[j][0])
            ans = max(ans, ans - sushi[j][1] + sushi[i][1] + len(kind) ** 2)
            kind.add(sushi[j][0])
    print(ans)

if __name__ == '__main__':
    main()