def main():
    n = int(input())
    x = []
    y = []
    h = []
    for _ in range(n):
        x1, y1, h1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    #print(x)
    #print(y)
    #print(h)
    #h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0) となるC_X, C_Y, Hを求める
    #h[i] = 0の場合はC_X, C_Y, Hの候補としては考慮しない
    #h[i] = 0でない場合はC_X, C_Y, Hの候補として考慮する
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y

if __name__ == '__main__':
    main()