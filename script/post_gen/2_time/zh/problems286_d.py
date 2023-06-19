Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    dp = [False] * (x + 1)
    dp[0] = True
    for i in range(n):
        for j in range(x + 1):
            if dp[j]:
                dp[j] = True
            elif j - a[i] >= 0 and dp[j - a[i]] and b[i] > 0:
                dp[j] = True
                b[i] -= 1

    if dp[x]:
        print('Yes')
    else:
        print('No')

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
    total = 0
    for i in range(N):
        total += A[i] * B[i]
    if total <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i] * B[i]
    if total <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a, b)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum < x:
        print("No")
    else:
        print("Yes")

solve()

=======
Suggestion 5

def solve():
    # 读取输入
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 算法
    for i in range(N):
        X -= A[i] * B[i]
    if X < 0:
        print("No")
    else:
        print("Yes")


solve()

=======
Suggestion 6

def canpay(x, a, b):
    if x == 0:
        return True
    elif x < 0 or len(a) == 0 or len(b) == 0:
        return False
    else:
        for i in range(b[0]+1):
            if canpay(x-a[0]*i, a[1:], b[1:]):
                return True
        return False

=======
Suggestion 7

def solve():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        X -= A[i]*B[i]
    if X < 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum > X:
        print("No")
    else:
        print("Yes")

main()

=======
Suggestion 9

def search(x, y, z):
    if x == 0:
        return True
    if y == 0:
        return False
    if x < z[0][0]:
        return False
    if x // z[0][0] <= z[0][1]:
        return search(x % z[0][0], y - 1, z[1:])
    else:
        return search(x - z[0][0] * z[0][1], y - 1, z[1:])

=======
Suggestion 10

def pay(N, X, A, B):
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum >= X:
        return True
    else:
        return False
