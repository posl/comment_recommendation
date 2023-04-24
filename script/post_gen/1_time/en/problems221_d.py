Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    for i in range(1, N + 1):
        print(D[i], end=' ')

=======
Suggestion 2

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0]*(N+1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i]+B[i]] -= 1
    for i in range(1, N+1):
        D[i] += D[i-1]
    D = D[1:]
    D.sort()
    print(" ".join(map(str, D)))

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    D = [0]*(N+1)
    for i in range(N):
        D[0] += A[i]-1
        D[0] -= max(0,A[i]+B[i]-10**100-1)
        D[1] += min(B[i],10**100-A[i]+1)
        D[min(B[i],N)] -= min(B[i],10**100-A[i]+1)
    for i in range(1,N+1):
        D[i] += D[i-1]
    print(*D[:N])

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = [0] * (N+1)
    for i in range(N):
        ans[0] += 1
        ans[0] -= 1
        ans[B[i]] += 1
    for i in range(N):
        ans[i+1] += ans[i]
    for i in range(N):
        print(ans[i],end=" ")
    print()

=======
Suggestion 5

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    D = [0] * (10**5 + 1)
    for a, b in AB:
        D[a] += 1
        D[a + b] -= 1

    for i in range(1, 10**5 + 1):
        D[i] += D[i - 1]

    print(*D[1:N + 1])

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = [0 for i in range(N+1)]
    for i in range(N):
        ans[A[i]] += 1
        ans[A[i]+B[i]] -= 1
    for i in range(1,N+1):
        ans[i] += ans[i-1]
    for i in range(1,N+1):
        print(ans[i],end=' ')
    print()
    return

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 1日目から最終日までの日数をカウントする配列を用意
    # 1日目から最終日まで、誰もログインしていない日数を数える
    # すべてのプレイヤーのログイン期間をカウントする
    # 1日目から最終日まで、ログインしているプレイヤーの数を数える
    # 1日目から最終日まで、ログインしているプレイヤーの数がk人になる日数を数える

    # 1日目から最終日までの日数をカウントする配列を用意
    days = [0] * 10**9

    # 1日目から最終日まで、誰もログインしていない日数を数える
    # すべてのプレイヤーのログイン期間をカウントする
    for i in range(N):
        # 1日目から最終日まで、誰もログインしていない日数を数える
        days[A[i]-1] += 1
        days[A[i]+B[i]-1] -= 1
        # すべてのプレイヤーのログイン期間をカウントする
        # days[A[i]-1] += 1
        # days[A[i]+B[i]-1] -= 1

    # 1日目から最終日まで、ログインしているプレイヤーの数を数える
    for i in range(1, 10**9):
        days[i] += days[i-1]

    # 1日目から最終日まで、ログインしているプレイヤーの数がk人になる日数を数え

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #A.append(0)
    #B.append(0)
    #N += 1
    #A, B = zip(*sorted(zip(A, B), key=lambda x: x[0]))
    #print(A)
    #print(B)
    #print(N)
    day = [0] * (10**9+2)
    for i in range(N):
        day[A[i]] += 1
        day[A[i]+B[i]] -= 1
    #print(day)
    for i in range(1, 10**9+2):
        day[i] += day[i-1]
    #print(day)
    day = day[1:-1]
    #print(day)
    day = sorted(day)
    #print(day)
    for i in range(N):
        print(day[i], end=" ")
    print()

=======
Suggestion 9

def main():
    N = int(input())
    B = []
    for _ in range(N):
        A,B = [int(i) for i in input().split()]
        B.append([A,B])
    B.sort()
    ans = [0]*(N+1)
    for i in range(N):
        ans[1] += B[i][0]-1
        ans[1] -= sum([B[j][1] for j in range(i)])
        ans[1] = max(ans[1],0)
        ans[1] = min(ans[1],B[i][1])
        ans[N] += B[i][0]-1
        ans[N] -= sum([B[j][1] for j in range(i)])
        ans[N] = max(ans[N],0)
        ans[N] = min(ans[N],B[i][1])
        ans[1] += 1
        ans[N] -= 1
        ans[B[i][1]] += 1
        ans[B[i][1]+1] -= 1
    for i in range(1,N):
        ans[i] += ans[i-1]
    for i in range(1,N+1):
        print(ans[i],end=" ")
    print()

=======
Suggestion 10

def solve(n, a, b):
    # write your code here
    # return your answer
    pass
