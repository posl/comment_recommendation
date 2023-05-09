def main():
    N, Q = map(int, input().split())
    # a, bを入力
    ab = []
    for i in range(N-1):
        ab.append(list(map(int, input().split())))
    #print(ab)
    # p, xを入力
    px = []
    for i in range(Q):
        px.append(list(map(int, input().split())))
    #print(px)
    # リストの初期化
    ans = [0] * (N+1)
    #print(ans)
    # p, xのリストを作成
    for i in range(Q):
        ans[px[i][0]] += px[i][1]
        #print(ans)
    #print(ans)
    # a, bのリストを作成
    for i in range(N-1):
        ans[ab[i][1]] += ans[ab[i][0]]
        #print(ans)
    #print(ans)
    # 出力
    for i in range(1, N+1):
        print(ans[i], end=" ")
    print("")
