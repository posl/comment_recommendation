Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)

    # N = 10^9なので、N^2は10^18になる
    # 10^18はint型の最大値を超えるので、メモリが足りない
    # そのため、N×Nの行列を作るのは無理
    # そこで、N×Qの行列を作って、T_i=1のときはA_i行B_i列の要素を1にする
    # T_i=2のときはA_i行B_i列の要素を0にする
    # T_i=3のときはA_i行B_i列とB_i行A_i列の要素が両方とも1のときYes、そうでないときNoを出力する
    # このようにすれば、メモリの使用量はN×Qになる
    # また、T_i=1とT_i=2のときは、A_i行B_i列とB_i行A_i列の要素を同時に変更する必要がある
    # なので、T_i=1とT_i=2は同時に処理する
    # また、T_i=1とT_i=2のときは、A_i行B_i列とB_i行A_i列の要素を同時に変更する必要がある
    # なので、T_i=1とT_i=2は同時に処理する
    # また、T_i=1とT_i=2のときは、A_i行B_i列とB_i行A_i列の要素を同時に変更する必要がある
    # なので、T_i=1とT_i=2は同時に処理する

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    follow = [set() for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a - 1].add(b - 1)
        elif t == 2:
            follow[a - 1].discard(b - 1)
        else:
            print("Yes" if b - 1 in follow[a - 1] and a - 1 in follow[b - 1] else "No")

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = [0] * Q
    B = [0] * Q
    T = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    #print("N", N)
    #print("Q", Q)
    #print("A", A)
    #print("B", B)
    #print("T", T)
    #print("A[0]", A[0])
    #print("B[0]", B[0])
    #print("T[0]", T[0])
    #print("A[1]", A[1])
    #print("B[1]", B[1])
    #print("T[1]", T[1])
    #print("A[2]", A[2])
    #print("B[2]", B[2])
    #print("T[2]", T[2])
    #print("A[3]", A[3])
    #print("B[3]", B[3])
    #print("T[3]", T[3])
    #print("A[4]", A[4])
    #print("B[4]", B[4])
    #print("T[4]", T[4])
    #print("A[5]", A[5])
    #print("B[5]", B[5])
    #print("T[5]", T[5])
    #print("A[6]", A[6])
    #print("B[6]", B[6])
    #print("T[6]", T[6])
    #print("A[7]", A[7])
    #print("B[7]", B[7])
    #print("T[7]", T[7])
    #print("A[8]", A[8])
    #print("B[8]", B[8])
    #print("T[8]", T[8])
    #print("A[9]", A[9])
    #print("B[9]", B[9])
    #print("T[9]", T[9])
    #print("A[10]", A[10])
    #print("B[10]", B[10])
    #print("T[10]", T[

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    follow = [set() for i in range(N)]
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A - 1].add(B - 1)
        elif T == 2:
            follow[A - 1].discard(B - 1)
        else:
            if A - 1 in follow[B - 1] and B - 1 in follow[A - 1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    F = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            F[A-1].add(B-1)
        elif T == 2:
            F[A-1].discard(B-1)
        else:
            if B-1 in F[A-1] and A-1 in F[B-1]:
                print("Yes")
            else:
                print("No")
    return

=======
Suggestion 6

def solve():
    N, Q = map(int, input().split())
    follow = [[] for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A-1].append(B-1)
        elif T == 2:
            if B-1 in follow[A-1]:
                follow[A-1].remove(B-1)
        else:
            if A-1 in follow[B-1] and B-1 in follow[A-1]:
                print("Yes")
            else:
                print("No")

solve()

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = [set() for i in range(N)]
    B = [set() for i in range(N)]
    for i in range(Q):
        T, a, b = map(int, input().split())
        if T == 1:
            A[a - 1].add(b - 1)
            B[b - 1].add(a - 1)
        elif T == 2:
            if a - 1 in A[b - 1]:
                A[b - 1].remove(a - 1)
            if b - 1 in B[a - 1]:
                B[a - 1].remove(b - 1)
        else:
            if a - 1 in B[b - 1] and b - 1 in A[a - 1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())

    # フォローしている人の集合
    follow = [set() for _ in range(N)]
    # フォローされている人の集合
    follower = [set() for _ in range(N)]

    for _ in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            follow[A].add(B)
            follower[B].add(A)
        elif T == 2:
            follow[A].discard(B)
            follower[B].discard(A)
        else:
            if B in follow[A] and A in follow[B]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    pairs = []
    for i in range(Q):
        pairs.append(list(map(int, input().split())))
    #print(pairs)
    ans = []
    for i in range(Q):
        if pairs[i][0] == 3:
            if pairs[i][1] == pairs[i][2]:
                ans.append("Yes")
            else:
                ans.append("No")
        else:
            if pairs[i][0] == 1:
                pairs[i][0] = 2
            else:
                pairs[i][0] = 1
            for j in range(Q):
                if pairs[j][0] == 3:
                    if pairs[j][1] == pairs[i][1] and pairs[j][2] == pairs[i][2]:
                        ans.append("Yes")
                    elif pairs[j][1] == pairs[i][1] and pairs[j][2] == pairs[i][2]:
                        ans.append("Yes")
                    else:
                        ans.append("No")
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 10

def solve(n, q, t, a, b):
    # Write your code here
    # Return the correct answer - either "Yes" or "No" for each query of type 3
    # Return a list containing all the answers.
    return []
