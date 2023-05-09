def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    # 隣接リスト
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    # 標高の高い方から順に訪問していく
    ans = 0
    for i in range(N):
        flag = True
        for j in G[i]:
            if H[i] <= H[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()