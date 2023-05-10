Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 5
    a = [5,3,2,4,1]
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    print(b)

=======
Suggestion 2

def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    n = int(input())
    # スペース区切りの整数の入力
    p = list(map(int, input().split()))
    # 出力
    print(p)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)

=======
Suggestion 4

def main():
    N = int(input())
    P = []
    P = list(map(int, input().split()))
    Q = [0]*N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)
    return

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)
main()

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(" ".join(map(str,q)))

=======
Suggestion 8

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)
