def main():
    #入力
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    #正の面積を持つ三角形になるような点の選び方の総数を求める
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if X[i]*(Y[j]-Y[k])+X[j]*(Y[k]-Y[i])+X[k]*(Y[i]-Y[j]) != 0:
                    ans += 1
    #出力
    print(ans)
