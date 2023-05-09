def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((d, t))
    sushi.sort(reverse=True)
    kinds = set()
    kinds.add(sushi[0][1])
    base = sushi[0][0]
    bonus = len(kinds)**2
    ans = base+bonus
    for i in range(1, K):
        base += sushi[i][0]
        kinds.add(sushi[i][1])
        bonus = len(kinds)**2
        ans = max(ans, base+bonus)
    if K == N:
        print(ans)
        return
    for i in range(K, N):
        if sushi[i][1] in kinds:
            continue
        base += sushi[i][0]
        kinds.add(sushi[i][1])
        bonus = len(kinds)**2
        base -= sushi[K-1][0]
        kinds.remove(sushi[K-1][1])
        bonus -= len(kinds)**2
        ans = max(ans, base+bonus)
    print(ans)

if __name__ == '__main__':
    main()