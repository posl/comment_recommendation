Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K - Q] * N
    for i in A:
        score[i - 1] += 1
    for i in score:
        if i > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    b = [0] * n
    for i in range(q):
        b[a[i] - 1] += 1
    for i in range(n):
        if k - q + b[i] > 0:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 3

def main():
    n, k, q = map(int, input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    
    score = [k] * n
    for i in range(q):
        score[a[i]-1] += 1
    for i in range(n):
        if score[i] <= q:
            print('No')
        else:
            print('Yes')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    P = [K-Q for i in range(N)]
    for i in A:
        P[i-1] += 1
    for i in P:
        if i > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    # 读取输入
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    # 初始化
    s = [k - q] * n
    # 逐个减分
    for i in a:
        s[i - 1] += 1
    # 输出
    for i in s:
        if i > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    N, K, Q = map(int, input().split())
    A = []
    for i in range(Q):
        A.append(int(input()))
    B = [0] * N
    for i in range(Q):
        B[A[i] - 1] += 1
    for i in range(N):
        if K + B[i] - Q > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n, k, q = map(int, input().split())
    score = [k] * n
    for i in range(q):
        a = int(input())
        score[a-1] += 1
    for i in range(n):
        if score[i] <= q:
            print('No')
        else:
            print('Yes')

=======
Suggestion 8

def main():
    n,k,q = map(int,input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    b = [0 for i in range(n)]
    for i in range(q):
        b[a[i]-1]+=1
    for i in range(n):
        if k+ b[i] -q >0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    n,k,q = map(int, input().split())
    score = [k]*n
    for i in range(q):
        a = int(input())
        score[a-1] = score[a-1] - 1
    for i in score:
        if i > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    n, k, q = map(int, input().split())
    score = [0] * n
    for i in range(q):
        a = int(input())
        score[a-1] += 1
    for i in range(n):
        if score[i] + k - q > 0:
            print('Yes')
        else:
            print('No')
