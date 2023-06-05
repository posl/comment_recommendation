Synthesizing 9/10 solutions

=======
Suggestion 1

def solve():
    n,s,d = map(int,input().split())
    x = []
    y = []
    for i in range(n):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            break
    else:
        print('No')
solve()

=======
Suggestion 2

def isHurt(N, S, D, X, Y):
    for i in range(N):
        if X[i] < S and Y[i] > D:
            return True
    return False

=======
Suggestion 3

def judge():
    N,S,D = map(int,input().split())
    for i in range(N):
        X,Y = map(int,input().split())
        if X < S and Y > D:
            return "Yes"
    return "No"

=======
Suggestion 4

def solve():
    N, S, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def judge():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x<s and y>d:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 6

def solve():
    # 读入N，S，D
    N, S, D = map(int, input().split())
    # 读入X_i, Y_i
    XY = [list(map(int, input().split())) for _ in range(N)]
    # 用于记录是否存在满足条件的法术
    flag = False
    # 遍历N个法术
    for i in range(N):
        # 如果存在满足条件的法术，跳出循环
        if flag:
            break
        # 如果第i个法术的施展时间小于S并且威力大于D，跳过
        if XY[i][0] < S and XY[i][1] > D:
            continue
        # 遍历N个法术
        for j in range(N):
            # 如果第j个法术的施展时间大于S或者威力小于D，跳过
            if XY[j][0] > S or XY[j][1] < D:
                continue
            # 如果第i个法术的施展时间小于等于第j个法术的施展时间并且威力大于等于第j个法术的威力，跳过
            if XY[i][0] <= XY[j][0] and XY[i][1] >= XY[j][1]:
                continue
            # 如果存在满足条件的法术，跳出循环
            if flag:
                break
            # 如果第i个法术的施展时间小于等于第j个法术的施展时间并且威力大于等于第j个法术的威力，跳出循环
            if XY[i][0] <= XY[j][0] and XY[i][1] >= XY[j][1]:
                break
        # 如果不存在满足条件的法术，跳出循环
        if j == N - 1:
            break
    # 如果存在满足条件的法术，打印Yes

=======
Suggestion 7

def solve():
    N, S, D = map(int, input().split())
    for i in range(N):
        x, y = map(int, input().split())
        if x < S and y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def solve():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            print('Yes')
            return
    print('No')
solve()

=======
Suggestion 9

def main():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            print('Yes')
            exit()
    print('No')
