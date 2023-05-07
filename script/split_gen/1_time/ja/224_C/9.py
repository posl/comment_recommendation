def main():
    N = int(input()) #Nは整数である
    points = [] #座標を格納する配列
    for i in range(N): #N個の座標を入力する
        X,Y = map(int,input().split()) #X,Yは整数である
        points.append([X,Y]) #座標を配列に格納する
    count = 0 #三角形の数をカウントする変数
    for i in range(N): #N個の座標のうち一つ目の座標を選ぶ
        for j in range(i+1,N): #N個の座標のうち二つ目の座標を選ぶ
            for k in range(j+1,N): #N個の座標のうち三つ目の座標を選ぶ
                #三角形の面積を求める
                area = (points[i][0]*(points[j][1]-points[k][1]) + points[j][0]*(points[k][1]-points[i][1]) + points[k][0]*(points[i][1]-points[j][1]))/2
                if area > 0: #三角形の面積が正の場合
                    count += 1 #三角形の数をカウントする変数を1増やす
    print(count) #三角形の数を出力する
