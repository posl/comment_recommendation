Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    if total <= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        at, bt = map(int, input().split())
        a.append(at)
        b.append(bt)

    sum = 0
    for i in range(n):
        sum += a[i] * b[i]

    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 'No'
    for i in range(N):
        if A[i] <= X and B[i] > 0:
            ans = 'Yes'
            break
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(list(map(int, input().split())))
    coins.sort()
    coins.reverse()
    ans = 0
    for coin in coins:
        if coin[1] > 0:
            ans += coin[0]
            coin[1] -= 1
    if ans >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        aa, bb = map(int, input().split())
        a.append(aa)
        b.append(bb)

    total = 0
    for i in range(n):
        total += a[i] * b[i]

    if total <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n,x=map(int,input().split())
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=map(int,input().split())
    ans=0
    for i in range(n):
        ans+=a[i]*b[i]
    if ans<=x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(n)]
    a_b.sort(key=lambda x: x[0])
    #print(a_b)
    dp = [[False]*(x+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j + a_b[i][0] <= x:
                    dp[i+1][j+a_b[i][0]] = True
    if dp[n][x]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    coins = [list(map(int, input().split())) for _ in range(n)]
    coins.sort(key=lambda x: x[0])
    dp = [[0 for _ in range(x + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(x + 1):
            for k in range(coins[i][1] + 1):
                if j + coins[i][0] * k <= x:
                    dp[i + 1][j + coins[i][0] * k] += dp[i][j]
    print("Yes" if dp[n][x] > 0 else "No")

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = "No"
    for i in range(N):
        for j in range(B[i]):
            if X == 0:
                ans = "Yes"
                break
            X -= A[i]
        if ans == "Yes":
            break
    if X <= 0:
        ans = "Yes"
    print(ans)

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    total = 0
    for _ in range(n):
        a, b = map(int, input().split())
        total += a * b
    if total > x:
        print("No")
    else:
        print("Yes")
