Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    i = 0
    j = 0
    ans = []
    while i < N and j < N:
        if L[i] <= R[j]:
            l = L[i]
            i += 1
            while i < N and L[i] <= R[j]:
                i += 1
            r = R[j]
            j += 1
            while j < N and L[i-1] <= R[j]:
                j += 1
            ans.append([l,r])
    print(*ans, sep='

')

=======
Suggestion 2

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    ans = []
    for i in range(N):
        if L[i] < R[i]:
            ans.append([L[i], R[i]])

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 3

def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())

    #右端でソート
    sort = sorted([(R[i], L[i]) for i in range(N)])

    #右端の最初の値を格納
    right = sort[0][0]
    #左端の最初の値を格納
    left = sort[0][1]

    for i in range(1, N):
        #右端の値が前の左端の値よりも大きい場合
        if right <= sort[i][1]:
            #左端の値を更新
            left = sort[i][1]
            #右端の値を更新
            right = sort[i][0]

        #右端の値が前の左端の値よりも小さい場合
        elif right <= sort[i][0]:
            #右端の値を更新
            right = sort[i][0]

    print(left, right)

=======
Suggestion 4

def solve():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    i = 0
    j = 0
    ans = []
    while i < N and j < N:
        if L[i] < R[j]:
            ans.append([L[i], R[j]])
            i += 1
            j += 1
        else:
            j += 1
    for a in ans:
        print(a[0], a[1])
solve()

=======
Suggestion 5

def main():
    N = int(input())
    LR = []
    for _ in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort()
    X = LR[0][0]
    Y = LR[0][1]
    for i in range(1, N):
        if LR[i][0] <= Y:
            Y = max(Y, LR[i][1])
        else:
            print(X, Y)
            X = LR[i][0]
            Y = LR[i][1]
    print(X, Y)

=======
Suggestion 6

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort()
    X = []
    Y = []
    i = 0
    while i < N:
        j = i
        while j < N-1 and LR[j][1] >= LR[j+1][0]:
            j += 1
        X.append(LR[i][0])
        Y.append(LR[j][1])
        i = j + 1
    print(len(X))
    for i in range(len(X)):
        print(X[i], Y[i])

=======
Suggestion 7

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    LR.sort(key=lambda x: x[1])

    ans = []
    l = 0
    r = 0
    for i in range(N):
        if r < LR[i][0]:
            ans.append([l, r])
            l = LR[i][0]
            r = LR[i][1]
        else:
            r = max(r, LR[i][1])
    ans.append([l, r])
    ans.pop(0)

    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 8

def solve():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    i = 0
    while i < N:
        l, r = LR[i]
        while i < N - 1 and r >= LR[i + 1][0]:
            r = max(r, LR[i + 1][1])
            i += 1
        ans.append([l, r])
        i += 1
    print(len(ans))
    for l, r in ans:
        print(l, r)
    return

=======
Suggestion 9

def main():
    N = int(input())
    LR = [list(map(int,input().split())) for i in range(N)]
    LR.sort(key=lambda x:x[0])
    ans = []
    ans.append(LR[0])
    for i in range(1,N):
        if ans[-1][1] < LR[i][0]:
            ans.append(LR[i])
        elif ans[-1][1] < LR[i][1]:
            ans[-1][1] = LR[i][1]
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 10

def main():
    N = int(input())
    LR = []
    for i in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort()
    X = []
    Y = []
    #print(LR)
    X.append(LR[0][0])
    Y.append(LR[0][1])
    for i in range(1, N):
        if LR[i][0] <= Y[len(Y)-1]:
            Y[len(Y)-1] = max(Y[len(Y)-1], LR[i][1])
        else:
            X.append(LR[i][0])
            Y.append(LR[i][1])
    for i in range(len(X)):
        print(X[i], Y[i])
