def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    #各展望台の隣接リスト
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = 0
    for i in range(N):
        is_good = True
        for j in G[i]:
            if H[i] <= H[j]:
                is_good = False
                break
        if is_good:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()