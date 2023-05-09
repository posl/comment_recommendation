def main():
    #入力
    N, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #問題解決
    #原点からの距離がD以下であるような点の個数を求める
    #原点からの距離は(p^2+q^2)^(1/2)で表される
    #Dの2乗
    D2 = D**2
    #原点からの距離がD以下であるような点の個数
    cnt = 0
    for i in range(N):
        #p^2+q^2
        p2q2 = X[i]**2 + Y[i]**2
        if p2q2 <= D2:
            cnt += 1
    #出力
    print(cnt)
