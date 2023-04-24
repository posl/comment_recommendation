Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    follow = [set() for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[a-1].discard(b-1)
        else:
            if b-1 in follow[a-1] and a-1 in follow[b-1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    follow = [[0 for i in range(n)] for j in range(n)]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a - 1][b - 1] = 1
        elif t == 2:
            follow[a - 1][b - 1] = 0
        else:
            if follow[a - 1][b - 1] == 1 and follow[b - 1][a - 1] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 3

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = defaultdict(set)
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            G[a].add(b)
        elif t == 2:
            G[a].discard(b)
        else:
            print("Yes" if b in G[a] and a in G[b] else "No")

=======
Suggestion 4

def main():
    # Step #1. Input
    n, q = map(int, input().split())
    t = [0] * q
    a = [0] * q
    b = [0] * q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())

    # Step #2. Solve
    # Step #2-1. Initialize
    ans = [0] * q
    follow = [0] * n
    follower = [0] * n
    for i in range(q):
        if t[i] == 1:
            follow[a[i] - 1] += 1
            follower[b[i] - 1] += 1
        elif t[i] == 2:
            if follow[a[i] - 1] > 0:
                follow[a[i] - 1] -= 1
            if follower[b[i] - 1] > 0:
                follower[b[i] - 1] -= 1
        else:
            if follow[a[i] - 1] > 0 and follower[b[i] - 1] > 0:
                ans[i] = 1

    # Step #2-2. Output
    for i in range(q):
        if ans[i] == 1:
            print('Yes')
        elif t[i] == 3:
            print('No')

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    # 1-index
    follow = [[] for _ in range(N+1)]
    followed = [[] for _ in range(N+1)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A].append(B)
            followed[B].append(A)
        elif T == 2:
            if A in follow[B]:
                follow[B].remove(A)
            if B in followed[A]:
                followed[A].remove(B)
        else:
            if A in followed[B] and B in follow[A]:
                print("Yes")
            else:
                print("No")

main()

This is my solution. I created two lists, one for each direction of following. The first list is for following and the second list is for followed. Each list is indexed by the user ID. Each list contains the user ID of the users that are either following or followed by the user ID of the list.

The first two if statements are for the first two cases. The first if statement is for when the user is following another user. The second if statement is for when the user is unfollowing another user. The third if statement is for when the user is asking if two users are following each other. The third if statement checks if the user is following the other user and the other user is following the user. If both of these are true, then the user is following the other user and the other user is following the user, so the answer is Yes. Otherwise, the answer is No.

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    # フォロー関係を管理するリスト
    follow = [set() for _ in range(N)]
    # フォローの逆関係を管理するリスト
    follower = [set() for _ in range(N)]
    for _ in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        # フォロー関係の登録
        if T == 1:
            follow[A].add(B)
            follower[B].add(A)
        # フォロー関係の解除
        elif T == 2:
            follow[A].discard(B)
            follower[B].discard(A)
        # フォロー関係の判定
        else:
            if B in follow[A] and A in follow[B]:
                print("Yes")
            else:
                print("No")

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    # 1: follow, 2: unfollow
    t, a, b = [0]*q, [0]*q, [0]*q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())

    # 1: follow, 2: unfollow
    for i in range(q):
        if t[i] == 1:
            print('follow')
        elif t[i] == 2:
            print('unfollow')
        else:
            print('check')

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    # N = 10^9
    # Q = 2*10^5
    # T_i = 1,2,3, A_i = 1,2,3, B_i = 1,2,3
    # A_i != B_i
    # T_i = 3 がある
    # 1 <= i <= Q
    # 1 <= A_i <= N
    # 1 <= B_i <= N
    # 2 <= N <= 10^9
    # 1 <= Q <= 2*10^5
    # T_i = 1,2,3
    # T_i = 3 がある
    # A_i != B_i

    # 1 <= i <= Q
    # 1 <= A_i <= N
    # 1 <= B_i <= N
    # 2 <= N <= 10^9
    # 1 <= Q <= 2*10^5
    # T_i = 1,2,3
    # T_i = 3 がある
    # A_i != B_i

    # 1 <= i <= Q
    # 1 <= A_i <= N
    # 1 <= B_i <= N
    # 2 <= N <= 10^9
    # 1 <= Q <= 2*10^5
    # T_i = 1,2,3
    # T_i = 3 がある
    # A_i != B_i

    # 1 <= i <= Q
    # 1 <= A_i <= N
    # 1 <= B_i <= N
    # 2 <= N <= 10^9
    # 1 <= Q <= 2*10^5
    # T_i = 1,2,3
    # T_i = 3 がある
    # A_i != B_i

    # 1 <= i <= Q
    # 1 <= A_i <= N
    # 1 <= B_i <= N
    # 2 <= N <= 10^9
    # 1 <= Q <= 2*10^5
    # T_i = 1,2,3
