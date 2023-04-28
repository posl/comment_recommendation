Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        if i == 0:
            if X[i] <= T[i]:
                ans += A[i]
        else:
            if X[i] - X[i - 1] <= T[i] - T[i - 1]:
                ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())

    #print(N)
    #print(T)
    #print(X)
    #print(A)

    # 1. T_1 < T_2 < ... < T_N
    # 2. 0 < T_1
    # 3. T_N <= 10^5
    # 4. 0 <= X_i <= 4
    # 5. 1 <= A_i <= 10^9
    # 6. 1 <= N <= 10^5
    # 7. Takahashi is at coordinate 0 at time 0
    # 8. Takahashi can move on the line at a speed of at most 1.
    # 9. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
    # 10. The time it takes to catch a Snuke is negligible.

    # 1. Takahashi is at coordinate 0 at time 0
    # 2. Takahashi can move on the line at a speed of at most 1.
    # 3. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
    # 4. The time it takes to catch a Snuke is negligible.

    # 1. Takahashi is at coordinate 0 at time 0
    # 2. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.
    # 3. The time it takes to catch a Snuke is negligible.

    # 1. Takahashi is at coordinate 0 at time 0
    # 2. He can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it appears.

    # Takahashi can catch a Snuke appearing from a pit if and only if he is at the coordinate of that pit exactly when it

=======
Suggestion 3

def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    ans = 0
    for i in range(N):
        ans += A[i]
    for i in range(N):
        if i == 0:
            if T[i] < X[i]:
                ans -= A[i]
        else:
            if T[i] - T[i-1] < abs(X[i] - X[i-1]):
                ans -= A[i]
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())

    #print(T)
    #print(X)
    #print(A)

    #dp = [[0] * 5 for i in range(N+1)]
    #dp[0][0] = 0
    #dp[0][1] = 0
    #dp[0][2] = 0
    #dp[0][3] = 0
    #dp[0][4] = 0
    dp = [0] * 5
    for i in range(N):
        #for j in range(5):
        #    dp[i+1][j] = dp[i][j]
        dp2 = [0] * 5
        for j in range(5):
            dp2[j] = dp[j]
        #print(dp2)
        for j in range(5):
            #if dp[i+1][j] < dp[i][j]:
            #    dp[i+1][j] = dp[i][j]
            if dp2[j] < dp[j]:
                dp2[j] = dp[j]
            if j == X[i]:
                #if dp[i+1][j] < dp[i][j] + A[i]:
                #    dp[i+1][j] = dp[i][j] + A[i]
                if dp2[j] < dp[j] + A[i]:
                    dp2[j] = dp[j] + A[i]
            #if dp[i+1][j] < dp[i][j] + A[i]:
            #    dp[i+1][j] = dp[i][j] + A[i]
            if j > 0:
                #if dp[i+1][j-1] < dp[i][j]:
                #    dp[i+1][j-1] = dp[i][j]
                if dp2[j-1] < dp[j]:
                    dp2[j-1] = dp[j]
        #print(dp2)
        #dp = dp2
        for j in range(5):
            dp[j] = dp2[j]
        #

=======
Suggestion 5

def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())

    max_size = 0
    for i in range(N):
        if i == 0:
            max_size = A[i]
        else:
            max_size = max(max_size, A[i] + A[i - 1] - abs(X[i] - X[i - 1]) - (T[i] - T[i - 1]))

    print(max_size)

=======
Suggestion 6

def main():
    N = int(input())
    T = [0]
    X = [0]
    A = [0]
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    #print(T)
    #print(X)
    #print(A)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if X[i] == 0:
            dp[i] = dp[i-1] + A[i]
        else:
            dp[i] = max(dp[i-1], dp[i-X[i]] + A[i])
    print(dp[N])

=======
Suggestion 7

def main():
    n = int(input())
    snukes = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snukes.append((t, x, a))
    snukes.sort(key=lambda x: x[0])
    dp = [0] * 5
    for t, x, a in snukes:
        dp[x] = max(dp[x], max(dp[:x]) + a)
    print(max(dp))

=======
Suggestion 8

def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort()
    ans = 0
    for t, x, a in snuke:
        if t >= x:
            ans += a
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    Snukes = []
    for i in range(N):
        T, X, A = map(int, input().split())
        Snukes.append([T, X, A])
    Snukes.sort()
    Takahashi = 0
    for i in range(N):
        if Takahashi < Snukes[i][1]:
            Takahashi = Snukes[i][1]
        if Takahashi == Snukes[i][1]:
            Takahashi += 1
    return Takahashi - 1

print(solve())

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        A.append((t, x, a))

    B = []
    C = []
    for t, x, a in A:
        if x == 0:
            B.append((t, a))
        else:
            C.append((t, x, a))

    B.sort()
    C.sort()

    D = []
    for t, a in B:
        D.append((t, a))
    for t, x, a in C:
        D.append((t, a))

    D.sort()

    T = 0
    X = 0
    Y = 0
    for t, a in D:
        if t > T:
            if X > 0:
                Y += a
                X -= 1
                T = t
        if t == T:
            if X == 0:
                X = 4
                Y += a
                T += 1
                X -= 1
    print(Y)
