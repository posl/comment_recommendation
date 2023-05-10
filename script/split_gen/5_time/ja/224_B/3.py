def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    #前処理
    #累積和を求める
    #横方向
    for i in range(h):
        for j in range(w-1):
            a[i][j+1] += a[i][j]
    #縦方向
    for j in range(w):
        for i in range(h-1):
            a[i+1][j] += a[i][j]
    #組み合わせを全探索
    for i1 in range(h-1):
        for i2 in range(i1+1, h):
            for j1 in range(w-1):
                for j2 in range(j1+1, w):
                    if a[i2][j2] - a[i1][j2] - a[i2][j1] + a[i1][j1] == 0:
                        print("Yes")
                        return
    print("No")
