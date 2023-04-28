Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    min_time = 10 ** 9 * 2 * N
    for i in range(N):
        time = 0
        for j in range(N):
            if j <= i:
                time += A[j] + B[j]
            else:
                time += B[j]
        #print("i = ", i, "time = ", time)
        if min_time > time:
            min_time = time
    print(min_time * X)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 10**18
    for i in range(n):
        tmp = x * a[i] + b[i] * (n - x)
        if ans > tmp:
            ans = tmp
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]

    def check(t):
        dp = [float('inf')] * (N + 1)
        dp[0] = 0
        for i in range(N):
            dp[i + 1] = min(dp[i + 1], dp[i] + A[i])
            dp[i + 1] = min(dp[i + 1], dp[max(0, i - X + 1)] + B[max(0, i - X + 1)])
        return dp[N] <= t

    ok = 10**18
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X:
            print(ans)
            return
    print(ans)

=======
Suggestion 6

def main():
    # input
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # compute
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += X * min([AB[i][1] for i in range(N)])

    # output
    print(ans)

=======
Suggestion 7

def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X * AB[i][1]:
            ans = X * AB[i][1]
        X -= 1
        if X == 0:
            break
    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])

    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i+1)
            return
    print(N+1)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]

    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i + 1)
            exit()
    print(N)

=======
Suggestion 10

def solve(n, x, ab):
    ab.sort(key=lambda x: x[0] + x[1])
    t = 0
    for a, b in ab:
        t += a + b
        if t > x:
            return "No"
    return "Yes"
