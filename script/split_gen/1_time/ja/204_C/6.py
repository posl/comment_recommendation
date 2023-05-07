def main():
    #入力
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    #グラフの構築
    G = [[] for _ in range(N)]
    for a,b in AB:
        G[a-1].append(b-1)
    #全ての都市の組み合わせについて、スタート地点とゴール地点の組として考えられるものの個数をカウント
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if i in G[j]:
                ans += 1
    print(ans)
