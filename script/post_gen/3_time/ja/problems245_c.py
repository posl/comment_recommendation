Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if i == 0:
            X[i] = min(A[i], B[i])
        else:
            if abs(A[i] - X[i-1]) <= K and abs(B[i] - X[i-1]) <= K:
                X[i] = min(A[i], B[i])
            elif abs(A[i] - X[i-1]) <= K:
                X[i] = A[i]
            elif abs(B[i] - X[i-1]) <= K:
                X[i] = B[i]
            else:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    X = [0] * N
    for i in range(N):
        if i == 0:
            if A[i] <= B[i]:
                X[i] = A[i]
            else:
                X[i] = B[i]
        else:
            if X[i - 1] + K >= A[i]:
                X[i] = A[i]
            elif X[i - 1] + K >= B[i]:
                X[i] = B[i]
            else:
                print("No")
                return
    print("Yes")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N == 1:
        print('Yes')
        return
    if A[0] == B[0]:
        if N == 2:
            print('Yes')
            return
        else:
            for i in range(1, N):
                if abs(A[i] - A[i - 1]) > K:
                    print('No')
                    return
            print('Yes')
            return
    else:
        for i in range(1, N):
            if abs(A[i] - A[i - 1]) > K and abs(B[i] - B[i - 1]) > K and abs(A[i] - B[i]) > K:
                print('No')
                return
        print('Yes')
        return

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N == 1:
        if abs(A[0]-B[0]) <= K:
            print("Yes")
        else:
            print("No")
        return
    if A[0] == B[0]:
        if abs(A[1]-B[1]) <= K:
            print("Yes")
        else:
            print("No")
        return
    if abs(A[0]-B[0]) <= K:
        print("Yes")
        return
    if abs(A[0]-B[0]) > K:
        print("No")
        return

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [abs(a[i] - b[i]) for i in range(n)]
    if max(c) > k:
        print("No")
        return
    if sum(c) % 2 == k % 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = [0]*N
    for i in range(N):
        if i==0:
            if A[i] > B[i]:
                X[i] = B[i]
            else:
                X[i] = A[i]
        else:
            if A[i] > B[i]:
                if B[i] <= X[i-1]+K:
                    X[i] = B[i]
                else:
                    X[i] = A[i]
            else:
                if A[i] <= X[i-1]+K:
                    X[i] = A[i]
                else:
                    X[i] = B[i]
    if X[N-1] - X[0] <= K:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(N-1):
        if abs(A[i]-A[i+1])>K and abs(B[i]-B[i+1])>K:
            if abs(A[i]-B[i+1])>K and abs(B[i]-A[i+1])>K:
                print("No")
                return
            else:
                if A[i]>B[i]:
                    A[i+1] = B[i+1]
                else:
                    B[i+1] = A[i+1]
        else:
            if abs(A[i]-B[i+1])<=K:
                A[i+1] = B[i+1]
            if abs(B[i]-A[i+1])<=K:
                B[i+1] = A[i+1]
    if A == B:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = []
    for a,b in zip(A,B):
        X.append([a,b])
    for i in range(N-1):
        if abs(X[i][0]-X[i+1][0]) <= K:
            X[i+1][0] = X[i][0]
        if abs(X[i][0]-X[i+1][1]) <= K:
            X[i+1][1] = X[i][0]
        if abs(X[i][1]-X[i+1][0]) <= K:
            X[i+1][0] = X[i][1]
        if abs(X[i][1]-X[i+1][1]) <= K:
            X[i+1][1] = X[i][1]
    if X[-1][0] == X[-1][1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = [0] * N

    #Xの初期値を決める
    for i in range(N):
        if A[i] <= B[i]:
            X[i] = A[i]
        else:
            X[i] = B[i]

    #Xを決める
    for i in range(N-1):
        if X[i] == A[i] and X[i+1] == A[i+1]:
            if abs(A[i]-B[i]) <= K:
                X[i+1] = B[i+1]
            else:
                X[i+1] = A[i+1]
        elif X[i] == B[i] and X[i+1] == B[i+1]:
            if abs(A[i]-B[i]) <= K:
                X[i+1] = A[i+1]
            else:
                X[i+1] = B[i+1]
        else:
            continue

    #Xを出力する
    for i in range(N):
        print(X[i],end=" ")
    print()

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #AとBが同じ値の場合は、その値でXを作れる
    for i in range(N):
        if A[i] == B[i]:
            continue
        #AとBの値が異なる場合、AとBの値の差がKを超える場合は、Xを作れない
        if abs(A[i] - B[i]) > K:
            print('No')
            return
    #AとBの値が異なる場合、AとBの値の差がKを超えない場合は、Xを作れる
    print('Yes')
