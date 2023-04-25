Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if ((i>>j)&1):
                sum += A[j]*B[j]
        if sum == X:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        if A[i] <= X:
            X -= A[i]
            B[i] -= 1
    for i in range(N):
        if B[i] >= 1:
            if A[i] <= X:
                X -= A[i]
                B[i] -= 1
    if X == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(N):
        for j in range(X + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i + 1][j - A[i]] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]
    if dp[N][X] > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for i in range(n):
        if x - a[i] * b[i] >= 0:
            x -= a[i] * b[i]
        else:
            x -= (x // a[i]) * a[i]
    if x == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    for i in range(N):
        if A[i]*B[i] >= X:
            B[i] = X//A[i]
            X -= A[i]*B[i]
        else:
            X -= A[i]*B[i]

    if X == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = "No"
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if ((i >> j) & 1):
                tmp += a[j]*b[j]
        if tmp == x:
            ans = "Yes"
    print(ans)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        if x >= a[i]:
            x -= a[i] * b[i]
        else:
            x -= a[i]
    if x > 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        for j in range(B[i]):
            X -= A[i]
            if X == 0:
                print('Yes')
                return
    print('No')

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    for i in range(2**N):
        temp = 0
        for j in range(N):
            if (i>>j)&1:
                temp += A[j]*B[j]
        if temp == X:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(a[i][1]):
            b.append(a[i][0])
    if sum(b) == x:
        print("Yes")
    else:
        print("No")
