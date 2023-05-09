def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((d, t))
    sushi.sort(reverse=True)
    sushi_set = set()
    ans = 0
    for i in range(K):
        ans += sushi[i][0]
        sushi_set.add(sushi[i][1])
    ans += len(sushi_set)**2
    for i in range(K, N):
        if sushi[i][1] in sushi_set:
            continue
        for j in range(K):
            if sushi[j][1] not in sushi_set:
                continue
            sushi_set.remove(sushi[j][1])
            sushi_set.add(sushi[i][1])
            ans = max(ans, ans - sushi[j][0] + sushi[i][0] + len(sushi_set)**2)
            break
    print(ans)

if __name__ == '__main__':
    main()