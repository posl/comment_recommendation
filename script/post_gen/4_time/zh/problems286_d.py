Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int, input().split())
    total = 0
    for i in range(n):
        a,b = map(int, input().split())
        total += a * b
        if total > x * 100:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    a_b = [list(map(int,input().split())) for _ in range(n)]
    a_b.sort(key=lambda x:x[0])
    #print(a_b)
    dp = [[0]*(x+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(x+1):
            if j == 0:
                dp[i+1][j] = 1
            elif j >= a_b[i][0]:
                dp[i+1][j] = dp[i][j] or dp[i+1][j-a_b[i][0]]
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print('Yes' if dp[n][x] else 'No')

=======
Suggestion 3

def pay(x, coins, remain):
    if x == 0:
        return True
    if remain == 0:
        return False
    if x < 0:
        return False
    return pay(x, coins, remain - 1) or pay(x - coins[remain - 1], coins, remain - 1)

n, x = map(int, input().split())
coins = []
for i in range(n):
    a, b = map(int, input().split())
    coins.append(a * b)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # print(A, B)
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def is_payable(n, x, a, b):
    if n == 1:
        if x % a[0] == 0 and x / a[0] <= b[0]:
            return True
        else:
            return False
    else:
        for i in range(b[0] + 1):
            if is_payable(n - 1, x - a[0] * i, a[1:], b[1:]):
                return True
        return False

=======
Suggestion 6

def solve():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    ans = 0
    for i in range(n):
        ans += a[i]*b[i]
    if ans <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    coins = [list(map(int,input().split())) for _ in range(n)]
    coins.sort()
    #print(coins)
    dp = [[0]*(x+1) for _ in range(n+1)]
    #print(dp)
    dp[0][0] = 1
    for i in range(n):
        for j in range(x+1):
            if j-coins[i][0]>=0:
                dp[i+1][j] = dp[i][j] | dp[i+1][j-coins[i][0]]
            else:
                dp[i+1][j] = dp[i][j]
    if dp[-1][-1]:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 8

def pay():
    n,x=map(int,input().split())
    a=[]
    b=[]
    for i in range(n):
        a1,b1=map(int,input().split())
        a.append(a1)
        b.append(b1)
    sum=0
    for i in range(n):
        sum+=a[i]*b[i]
    if sum<=x:
        print('Yes')
    else:
        print('No')
pay()

=======
Suggestion 9

def check_coins(coins, money):
    if money == 0:
        return True
    if money < 0:
        return False
    if len(coins) == 0:
        return False
    #print(coins, money)
    return check_coins(coins[1:], money) or check_coins(coins[1:], money - coins[0])

=======
Suggestion 10

def solve():
    N,X=map(int,input().split())
    A=[]
    B=[]
    for i in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        X-=A[i]*B[i]
    if X>=0:
        print("Yes")
    else:
        print("No")
