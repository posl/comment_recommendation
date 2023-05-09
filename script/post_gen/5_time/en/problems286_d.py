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

    sum = 0
    for i in range(N):
        sum += A[i] * B[i]

    if sum >= X:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 2

def readinput():
    n,x=list(map(int,input().split()))
    ab=[]
    for _ in range(n):
        ab.append(list(map(int,input().split())))
    return n,x,ab

=======
Suggestion 3

def main():
    N,X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i]*B[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    ans = "No"
    for i in range(n):
        if a[i] <= x and b[i] > 0:
            ans = "Yes"
    print(ans)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())

    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    res = 0
    for i in range(n):
        res += a[i] * b[i]
        if res > x * 100:
            print('No')
            return

    if res < x:
        print('No')
    else:
        print('Yes')

main()

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    amount = 0
    for i in range(N):
        A, B = map(int, input().split())
        amount += A * B
        if amount > X * 100:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(list(map(int, input().split())))
    total = 0
    for i in range(n):
        total += coins[i][0] * coins[i][1]
    if total <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    coins = []
    for _ in range(N):
        A, B = map(int, input().split())
        coins.append((A, B))
    coins.sort()
    ans = 0
    for A, B in coins:
        ans += A * B
        if ans > X * 100:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def solve():
    N, X = map(int, input().split())
    coins = [list(map(int, input().split())) for _ in range(N)]
    coins = sorted(coins, key=lambda x: x[0])
    total = 0
    for i in range(N):
        total += coins[i][0] * coins[i][1]
        if total > X:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def solve():
    n, x = map(int, input().split())
    coins = [list(map(int, input().split())) for _ in range(n)]
    coins.sort(key=lambda x: x[0])
    dp = [[False for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x+1):
            if not dp[i][j]:
                continue
            for k in range(coins[i][1]+1):
                if j + coins[i][0] * k > x:
                    break
                dp[i+1][j+coins[i][0]*k] = True
    print("Yes" if dp[n][x] else "No")
solve()
