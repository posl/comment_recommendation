Synthesizing 10/10 solutions (Duplicates hidden)

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
    time = T
    for i in range(N-1):
        time -= A[i]
        #print("time", time)
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+1:
                time += Y[j]
                #print("time", time)
        if time > T:
            time = T
    print("Yes")

=======
Suggestion 3

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
            if i+1 == X[j]:
                time += Y[j]
                break
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

    # 部屋1から部屋Nにたどり着けるかどうかを判定する
    # 部屋1から部屋2に移動するとき、部屋2に到着した時点での持ち時間がT以下かどうかを判定する
    # 部屋2から部屋3に移動するとき、部屋3に到着した時点での持ち時間がT以下かどうかを判定する
    # 部屋3から部屋4に移動するとき、部屋4に到着した時点での持ち時間がT以下かどうかを判定する
    # 部屋N-1から部屋Nに移動するとき、部屋Nに到着した時点での持ち時間がT以下かどうかを判定する
    # これらの判定をすべて満たす場合はYes、満たさない場合はNoを出力する

    # 部屋1から部屋2に移動するとき、部屋2に到着した時点での持ち時間がT以下かどうかを判定する
    # 部屋2に到着した時点での持ち時間は、部屋1に到着した時点での持ち時間から部屋1から部屋2に移動するために消費した時間を引いた値
    # 部屋1に到着した時点での持ち時間がT以下かどう

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
    #print(X)
    #print(Y)
    t = T
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+1:
                t += Y[j]
                break
    print("Yes")

=======
Suggestion 6

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(M):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(

=======
Suggestion 7

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        for j in range(M):
            if i+1 == X[j]:
                time += Y[j]
    print("Yes")

=======
Suggestion 8

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    bonus = []
    for i in range(M):
        bonus.append(list(map(int, input().split())))
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print('No')
            return
        for j in range(M):
            if i+1 == bonus[j][0]:
                time += bonus[j][1]
    print('Yes')

=======
Suggestion 9

def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    bonus = [0] * N
    for _ in range(M):
        X, Y = map(int, input().split())
        bonus[X - 1] = Y

    time = T
    for i in range(N - 1):
        time -= A[i]
        if time <= 0:
            print("No")
            return
        time += bonus[i]
    print("Yes")
