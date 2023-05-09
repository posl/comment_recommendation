def main():
    #入力
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #処理
    ans = 0
    for i in range(N):
        for j in range(1, L[i][0]+1):
            if X % L[i][j] == 0:
                ans += 1
    #出力
    print(ans)
