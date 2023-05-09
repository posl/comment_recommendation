def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #グラフ作成
    G = [[] for i in range(N)]
    for i in range(N-1):
        G[i].append(i+1)
        G[i+1].append(i)
    G[X-1].append(Y-1)
    G[Y-1].append(X-1)
    #print(G)
    #距離を求める
    for k in range(N-1):
        ans = 0
        for i in range(N):
            for j in range(i+1, N):
                if len(G[i])>len(G[j]):
                    i, j = j, i
                if j in G[i]:
                    ans += 1
                else:
                    for l in range(len(G[i])):
                        if G[i][l] in G[j]:
                            ans += 1
                            break
        print(ans)
        #print(k, ans)

if __name__ == '__main__':
    main()