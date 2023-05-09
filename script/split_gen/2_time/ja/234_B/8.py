def main():
    #入力
    N = int(input())
    xy = [list(map(int, input().split())) for i in range(N)]
    #最大値の初期化
    max = 0
    #二重ループで全ての組み合わせを試す
    for i in range(N):
        for j in range(i+1,N):
            #長さの計算
            l = ((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5
            #最大値の更新
            if l > max:
                max = l
    #出力
    print(max)
