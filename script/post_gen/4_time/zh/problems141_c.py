Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    N, K, Q = map(int, input().split())
    # print("N, K, Q:", N, K, Q)
    A = []
    for i in range(Q):
        A.append(int(input()))
    # print("A:", A)
    # 计算
    # 初始化
    score = [K] * N
    # print("score:", score)
    # 开始答题
    for i in range(Q):
        score[A[i] - 1] -= 1
    # print("score:", score)
    # 判断是否幸存
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def problem141_c():
    n, k, q = map(int, input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    b = [0] * n
    for i in range(q):
        b[a[i] - 1] += 1
    for i in range(n):
        if k - q + b[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    S = [K-Q for _ in range(N)]
    for i in range(Q):
        S[A[i]-1] += 1
    for i in range(N):
        if S[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    n,k,q = map(int,input().split())
    a = [0]*n
    for i in range(q):
        a[int(input())-1] += 1
    for i in range(n):
        if k - q + a[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    score = [K-Q for i in range(N)]
    for i in range(Q):
        score[A[i]-1] += 1
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    S = [K-Q for i in range(N)]
    for i in range(Q):
        S[A[i]-1] += 1
    for i in range(N):
        if S[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n, k, q = map(int, input().split())
    a = [0] * n
    for i in range(q):
        a[int(input()) - 1] += 1

    for i in range(n):
        if k - (q - a[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    n,k,q = map(int,input().split())
    score = [k]*n
    for i in range(q):
        a = int(input())
        score[a-1] += 1
    for i in range(n):
        if score[i] - q > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    count = [0] * N
    for i in range(Q):
        count[A[i]-1] += 1
    for i in range(N):
        if K - (Q - count[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    n,k,q = map(int,input().split())
    player = [0]*n
    for i in range(q):
        player[int(input())-1] += 1
    for i in range(n):
        if k - q + player[i] > 0:
            print('Yes')
        else:
            print('No')
