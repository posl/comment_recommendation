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
    print('Yes' if any(X % a == 0 and X // a <= N or X % b == 0 and X // b <= N or X % a == 0 and X % b == 0 and X // a + X // b <= N for a, b in zip(A, B)) else 'No')

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort(reverse=True)
    if X < A[0] or X > B[0]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        if A[i] <= X:
            X = B[i]
        elif B[i] <= X:
            X = A[i]
    if X == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X + 1):
            if dp[j]:
                dp[j + a[i]] = True
                dp[j + b[i]] = True
    if dp[X]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        X -= a[i]
        if X < 0:
            print("No")
            break
        if X == 0:
            print("Yes")
            break
        X -= b[i]
        if X < 0:
            print("No")
            break
        if X == 0:
            print("Yes")
            break
    if X > 0:
        print("No")

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        if X >= a[i]:
            X -= a[i]
        elif X >= b[i]:
            X -= b[i]
    if X == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    a = [0]*N
    b = [0]*N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    
    for i in range(N):
        X -= min(X, a[i])
        X -= min(X, b[i])
    
    if X == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        X = X - A[i]
        if X <= 0:
            print("No")
            return
        X = X + B[i]
        if X >= 10000:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    for i in range(n):
        if x <= a[i]:
            x = a[i]
        elif x <= b[i]:
            x = b[i]

    print('Yes' if x == x else 'No')

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = "No"
    for i in range(2**N):
        s = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j][1]
            else:
                s += A[j][0]
        if s == X:
            ans = "Yes"
    print(ans)
