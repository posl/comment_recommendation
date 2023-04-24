Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    follow = [[0] * N for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a][b] = 1
        elif t == 2:
            follow[b][a] = 1
        else:
            for i in range(N):
                if follow[i][a] == 1:
                    follow[i][b] = 1
            for i in range(N):
                if follow[b][i] == 1:
                    follow[a][i] = 1
            if follow[a][b] == 1:
                print('Yes')
            else:
                print('No')

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    follow = [set() for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[b].add(a)
        else:
            if a in follow[b]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    follow = [[0 for i in range(N)] for j in range(N)]
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a - 1][b - 1] = 1
        elif t == 2:
            follow[b - 1][a - 1] = 1
        else:
            for j in range(N):
                if follow[b - 1][j] == 1:
                    follow[a - 1][j] = 1
            for j in range(N):
                if follow[a - 1][j] == 1:
                    follow[j][a - 1] = 1
            if follow[a - 1][b - 1] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 4

def solve():
    N, Q = map(int, input().split())
    follow = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            follow[A].add(B)
        elif T == 2:
            follow[B].add(A)
        else:
            if B in follow[A]:
                print("Yes")
            elif A in follow[B]:
                print("Yes")
            else:
                print("No")

solve()

import sys
input = sys.stdin.readline

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    F = [[0] * N for _ in range(N)]
    for i in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            F[A][B] = 1
        elif T == 2:
            F[B][A] = 1
            for j in range(N):
                if F[j][A] == 1:
                    F[j][B] = 1
        else:
            if F[A][B] == 1:
                print('Yes')
            else:
                print('No')

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    # 2 ≦ N ≦ 10 ^ 9
    # 1 ≦ Q ≦ 2×10 ^ 5
    # T _ i=1,2,3 (1≦ i≦ Q)
    # 1 ≦ A _ i ≦ N (1≦ i≦ Q)
    # 1 ≦ B _ i ≦ N (1≦ i≦ Q)
    # A _ i≠ B _ i (1≦ i≦ Q)
    # T _ i=3 となる i (1≦ i≦ Q) が存在する
    # 入力される値はすべて整数
    # T _ i=1,2,3 (1≦ i≦ Q)
    # 1 ≦ A _ i ≦ N (1≦ i≦ Q)
    # 1 ≦ B _ i ≦ N (1≦ i≦ Q)
    # A _ i≠ B _ i (1≦ i≦ Q)
    # T _ i=3 となる i (1≦ i≦ Q) が存在する
    # 入力される値はすべて整数
    # T _ i=1,2,3 (1≦ i≦ Q)
    # 1 ≦ A _ i ≦ N (1≦ i≦ Q)
    # 1 ≦ B _ i ≦ N (1≦ i≦ Q)
    # A _ i≠ B _ i (1≦ i≦ Q)
    # T _ i=3 となる i (1≦ i≦ Q) が存在する
    # 入力される値はすべて整数
    # T _ i=1,2,3 (1≦ i≦ Q)
    # 1 ≦ A _ i ≦ N (1≦ i≦ Q)
    # 1 ≦ B _ i ≦ N (1≦ i≦ Q)
    # A _ i≠ B _ i (1≦ i≦ Q)

=======
Suggestion 7

def solve(n, q, t, a, b):
    follow = [set() for _ in range(n)]
    for i in range(q):
        if t[i] == 1:
            follow[a[i]-1].add(b[i]-1)
        elif t[i] == 2:
            follow[b[i]-1].add(a[i]-1)
        else:
            if a[i]-1 in follow[b[i]-1]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    # あるユーザーがフォローしているユーザーを格納する
    follow = {}
    # あるユーザーをフォローしているユーザーを格納する
    followed_by = {}
    for i in range(1, N+1):
        follow[i] = set()
        followed_by[i] = set()
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A].add(B)
            followed_by[B].add(A)
        elif T == 2:
            if A in follow[B]:
                follow[B].remove(A)
            if B in followed_by[A]:
                followed_by[A].remove(B)
        else:
            # A が B をフォローしているかどうか
            if B in follow[A]:
                print("Yes")
            # A が B をフォローしていない場合、A が B をフォローしているユーザーを調べる
            else:
                # A が B をフォローしているユーザーを格納する
                follow_A_B = set()
                for user in follow[A]:
                    follow_A_B.add(user)
                    for user_2 in follow[user]:
                        follow_A_B.add(user_2)
                if B in follow_A_B:
                    print("Yes")
                else:
                    print("No")

=======
Suggestion 9

def main():
    N,Q = map(int,input().split())
    # 隣接行列の初期化
    matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(Q):
        T,A,B = map(int,input().split())
        if T == 1:
            matrix[A-1][B-1] = 1
        elif T == 2:
            matrix[B-1][A-1] = 1
            for j in range(N):
                if matrix[j][A-1] == 1:
                    matrix[j][B-1] = 1
        else:
            if matrix[A-1][B-1] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    # 1. 1≦ i≦ N に対して、ユーザー i のフォローしているユーザーの集合を F _ i とする。
    # 2. 1≦ i≦ N に対して、ユーザー i にフォローされているユーザーの集合を B _ i とする。
    F = [[] for _ in range(N)]
    B = [[] for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            F[a].append(b)
            B[b].append(a)
        elif t == 2:
            if a in F[b]:
                F[b].remove(a)
                B[a].remove(b)
        else:
            if a in B[b]:
                print("Yes")
            else:
                print("No")
