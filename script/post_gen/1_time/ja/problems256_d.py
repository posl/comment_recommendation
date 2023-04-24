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
    ans = []
    for i in range(N - 1):
        if R[i] < L[i + 1]:
            ans.append([L[i], R[i]])
            L[i + 1] = L[i]
    ans.append([L[N - 1], R[N - 1]])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

main()

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

    for i in range(N):
        if L[i] != R[i]:
            print(L[i], R[i])
            return

=======
Suggestion 3

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

    # 1つの区間に収まる
    if L[N-1] == R[0]:
        print(L[N-1], R[0])

    # 2つの区間に分かれる
    else:
        print(L[0], R[N-1])

=======
Suggestion 4

def main():
    n = int(input())
    L = []
    R = []
    for i in range(n):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    l = L[0]
    r = R[0]
    for i in range(1, n):
        if l < L[i]:
            l = L[i]
        if r > R[i]:
            r = R[i]
    if l < r:
        print(l, r)
    else:
        print(0)

=======
Suggestion 5

def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    LR = list(zip(L, R))
    LR.sort(key=lambda x: x[0])
    ans = []
    ans.append(LR[0])
    for i in range(1, N):
        if ans[-1][1] < LR[i][0]:
            ans.append(LR[i])
        else:
            ans[-1] = (ans[-1][0], max(ans[-1][1], LR[i][1]))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for _ in range(N):
        L, R = map(int, input().split())
        S.append([L, R])
    S.sort()
    X = []
    Y = []
    for i in range(N):
        if i == 0:
            X.append(S[i][0])
            Y.append(S[i][1])
        else:
            if S[i][0] <= Y[-1]:
                Y[-1] = max(Y[-1], S[i][1])
            else:
                X.append(S[i][0])
                Y.append(S[i][1])
    for i in range(len(X)):
        print(X[i], Y[i])

=======
Suggestion 7

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for i in range(N)]
    LR.sort()
    ans = []
    ans.append(LR[0])
    for i in range(1, N):
        if ans[-1][1] >= LR[i][1]:
            continue
        elif ans[-1][1] >= LR[i][0]:
            ans[-1][1] = LR[i][1]
        else:
            ans.append(LR[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 8

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    for i in range(N):
        if i == 0:
            l, r = LR[i][0], LR[i][1]
            continue
        if LR[i][0] > r:
            ans.append([l, r])
            l, r = LR[i][0], LR[i][1]
        else:
            r = max(r, LR[i][1])
    ans.append([l, r])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 9

def main():
    N = int(input())
    LR = [list(map(int,input().split())) for i in range(N)]
    LR.sort(key=lambda x:x[0])
    ans = []
    l,r = LR[0]
    for i in range(1,N):
        if r >= LR[i][0]:
            r = max(r,LR[i][1])
        else:
            ans.append([l,r])
            l,r = LR[i]
    ans.append([l,r])
    for a in ans:
        print(*a)

=======
Suggestion 10

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x:x[0])
    ans = []
    for i in range(n):
        if len(ans) == 0:
            ans.append(l[i])
        else:
            if ans[-1][1] >= l[i][1]:
                continue
            elif ans[-1][1] >= l[i][0]:
                ans[-1][1] = l[i][1]
            else:
                ans.append(l[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
