def main():
    #入力
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #処理
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    if x[i] == x[j] and y[j] == y[k] and x[k] == x[l] and y[l] == y[i]:
                        ans += 1
    #出力
    print(ans)
