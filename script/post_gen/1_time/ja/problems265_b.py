Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+1:
                time += Y[j]
    print("Yes")

=======
Suggestion 2

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T)
    #print(A)
    #print(X)
    #print(Y)
    now = 0
    time = T
    for i in range(N-1):
        #print("now:%d time:%d" % (now, time))
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == now+1:
                time += Y[j]
        now += 1
    print("Yes")
    return

main()

=======
Suggestion 3

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())

    #print(N, M, T)
    #print(A)
    #print(X)
    #print(Y)

    #初期値
    t = T
    n = 1

    #print(t, n)

    #部屋1から部屋Nへ移動
    for i in range(N - 1):
        #print("i=", i)
        #print(t, n)
        #持ち時間を消費して部屋i+1へ移動
        t -= A[i]
        #print(t, n)
        #持ち時間が0以下になるような移動は行わない
        if t <= 0:
            print("No")
            return
        #部屋i+1に到達したらボーナス部屋かチェック
        if n == X[i]:
            t += Y[i]
        #print(t, n)
        #部屋i+1に到達したら部屋i+2に移動
        n += 1
        #print(t, n)
        #print()

    #最後の部屋へ移動した後に持ち時間が0以下になるような移動は行わない
    t -= A[N - 1]
    #print(t, n)
    if t <= 0:
        print("No")
        return

    print("Yes")

=======
Suggestion 4

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T)
    #print(A)
    #print(X)
    #print(Y)
    #print("------------")
    #print(A[0])
    #print("------------")
    #print(A[1])
    #print("------------")
    #print(A[2])
    #print("------------")
    #print(A[3])
    #print("------------")
    #print(A[4])
    #print("------------")
    #print(A[5])
    #print("------------")
    #print(A[6])
    #print("------------")
    #print(A[7])
    #print("------------")
    #print(A[8])
    #print("------------")
    #print(A[9])
    #print("------------")
    #print(A[10])
    #print("------------")
    #print(A[11])
    #print("------------")
    #print(A[12])
    #print("------------")
    #print(A[13])
    #print("------------")
    #print(A[14])
    #print("------------")
    #print(A[15])
    #print("------------")
    #print(A[16])
    #print("------------")
    #print(A[17])
    #print("------------")
    #print(A[18])
    #print("------------")
    #print(A[19])
    #print("------------")
    #print(A[20])
    #print("------------")
    #print(A[21])
    #print("------------")
    #print(A[22])
    #print("------------")
    #print(A[23])
    #print("------------")
    #print(A[24])
    #print("------------")
    #print(A[25])
    #print("------------")
    #print(A[26])
    #print("------------")
    #print(A[27])
    #print("------------")
    #print(A[28])
    #print("------------")
    #print(A[29])
    #print("------------")
    #print(A[30])
    #print("------------")

=======
Suggestion 5

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T)
    #print(A)
    #print(X, Y)
    #print("-----")
    #初期値
    time = T
    room = 1
    #print("time:", time, "room:", room)
    for i in range(N-1):
        #print("time:", time, "room:", room)
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if room == X[j]:
                time += Y[j]
        room += 1
    #print("time:", time, "room:", room)
    if time > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i],Y[i] = map(int,input().split())
    #print(N,M,T,A,X,Y)
    time = T
    for i in range(N-1):
        time -= A[i]
        #print(time)
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if i+1 == X[j]:
                time += Y[j]
                #print(time)
    print("Yes")

=======
Suggestion 7

def main():
    #入力
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #初期化
    now = 0
    time = T
    #処理
    for i in range(N-1):
        time -= A[i] #移動時間を減らす
        for j in range(M):
            if X[j] == i+1 and time + Y[j] > T:
                time = T #ボーナス部屋の処理
            elif X[j] == i+1:
                time += Y[j] #ボーナス部屋の処理
        if time <= 0:
            now = i+1 #移動できない部屋を記録
            break
    #出力
    if now == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    #入力
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #初期化
    t = T
    #処理
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+1:
                t += Y[j]
                break
    #出力
    if t > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # 入力
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    
    # 準備
    ans = "Yes"
    h = T
    for i in range(N-1):
        h -= A[i]
        if h <= 0:
            ans = "No"
            break
        for j in range(M):
            if i+1 == X[j]:
                h += Y[j]
                break
    # 出力
    print(ans)

=======
Suggestion 10

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
