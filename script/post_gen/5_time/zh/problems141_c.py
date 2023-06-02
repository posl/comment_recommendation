Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def solve():
    #n,k,q = map(int,input().split())
    #a = [int(input()) for _ in range(q)]
    n,k,q = 6,5,4
    a = [3,1,3,2]
    score = [k]*n
    for i in range(q):
        score[a[i]-1] -= 1
    for i in range(n):
        if score[i] <= 0:
            print('No')
        else:
            print('Yes')

=======
Suggestion 3

def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for i in range(Q)]
    #print(N,K,Q,A)
    ans = [0]*N
    for i in range(Q):
        ans[A[i]-1] += 1
    #print(ans)
    for i in range(N):
        if K+ans[i] - Q > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [0] * N
    for i in A:
        score[i-1] += 1
    for i in score:
        if K + i - Q > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K, Q = map(int, input().split())
    A = []
    for i in range(Q):
        A.append(int(input()))
    # print(N, K, Q, A)

    # 玩家的分数是（3，3，3，3，3，3）
    # 玩家3正确地回答了一个问题。现在玩家的分数是（2, 2, 3, 2, 2, 2）。
    # 玩家1正确地回答了一个问题。现在选手们的分数是（2, 1, 2, 1, 1, 1）。
    # 玩家3正确地回答了一个问题。现在选手们的分数是（1, 0, 2, 0, 0, 0）。
    # 玩家2正确地回答了一个问题。现在玩家的分数是（0, 0, 1, -1, -1, -1）。
    # 玩家1、2、4、5、6的分数为0或更低，被淘汰，玩家3在这场比赛中幸存。

    # 玩家的分数是（3，3，3，3，3，3）
    # 玩家3正确地回答了一个问题。现在玩家的分数是（2, 2, 3, 2, 2, 2）。
    # 玩家1正确地回答了一个问题。现在选手们的分数是（2, 1, 2, 1, 1, 1）。
    # 玩家3正确地回答了一个问题。现在选手们的分数是（1, 0, 2, 0, 0, 0）。
    # 玩家2正确地回答了一个问题。现在玩家的分数是（0, 0, 1, -1, -1, -1）。
    # 玩家1、2、4

=======
Suggestion 7

def main():
    N, K, Q = input().split()
    N = int(N)
    K = int(K)
    Q = int(Q)
    A = []
    for i in range(Q):
        A.append(int(input()))

    # print(N, K, Q)
    # print(A)
    # print("end")
    # print("N = ", N)
    # print("K = ", K)
    # print("Q = ", Q)
    # print("A = ", A)

    #初始化分数
    score = []
    for i in range(N):
        score.append(K)
    # print("score = ", score)

    #开始游戏
    for i in range(Q):
        # print("A[", i, "] = ", A[i])
        for j in range(N):
            if j != (A[i] - 1):
                # print("j = ", j)
                score[j] = score[j] - 1
        # print("score = ", score)

    #判断是否幸存
    for i in range(N):
        if score[i] <= 0:
            print("No")
        else:
            print("Yes")

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K-Q] * N
    for a in A:
        scores[a-1] += 1
    for score in scores:
        if score > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    scores = [k - q for _ in range(n)]
    for i in a:
        scores[i - 1] += 1
    for i in scores:
        if i > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    # 读取N,K,Q
    N,K,Q = map(int, input().split())
    # 读取A_i
    A_i = [int(input()) for i in range(Q)]
    # 初始化玩家分数
    score = [K for i in range(N)]
    # 玩家分数变化
    for i in range(Q):
        score[A_i[i]-1] -= 1
    # 判断玩家是否幸存
    for i in range(N):
        if score[i] <= 0:
            print('No')
        else:
            print('Yes')
