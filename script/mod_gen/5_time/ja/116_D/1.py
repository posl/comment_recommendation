def solve():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    used = set()
    base = 0
    for i in range(K):
        base += sushi[i][1]
        used.add(sushi[i][0])
    #print(base)
    ans = base + len(used)**2
    #print(ans)
    for i in range(K, N):
        if sushi[i][0] not in used:
            used.add(sushi[i][0])
            base -= sushi[i-K][1]
            base += sushi[i][1]
            ans = max(ans, base + len(used)**2)
    print(ans)

if __name__ == '__main__':
    solve()