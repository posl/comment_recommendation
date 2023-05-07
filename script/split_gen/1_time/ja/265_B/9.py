def main():
    #入力
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    bonus = []
    for i in range(M):
        bonus.append(list(map(int,input().split())))
    #print(N,M,T)
    #print(A)
    #print(bonus)
    #部屋1から部屋Nへの移動時間を計算
    time = 0
    for i in range(N-1):
        time += A[i]
        #print(time)
        #ボーナス部屋に到達したら持ち時間を増やす
        for j in range(M):
            if i+1 == bonus[j][0]:
                time += bonus[j][1]
                #print(time)
    #print(time)
    #部屋1から部屋Nへの移動時間が持ち時間Tを超えていなければYes
    if time <= T:
        print("Yes")
    else:
        print("No")
