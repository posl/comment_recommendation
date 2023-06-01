Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(x,y):
    if (x+y)%3 != 0:
        return 0
    else:
        n = int((2*y-x)/3)
        m = int((2*x-y)/3)
        if n<0 or m<0:
            return 0
        else:
            return comb(n+m,n,10**9+7)

=======
Suggestion 2

def move(x,y):
    count = 0
    if x == 0 and y == 0:
        return 1
    if x >= 1 and y >= 2:
        count += move(x-1,y-2)
    if x >= 2 and y >= 1:
        count += move(x-2,y-1)
    return count

=======
Suggestion 3

def main():
    x,y=map(int,input().split())
    x,y=abs(x),abs(y)
    if x+y==0:
        print(0)
        return
    if x+y==1:
        print(1)
        return
    if x+y==2:
        print(2)
        return
    if x<y:
        x,y=y,x
    if x==2 and y==2:
        print(0)
        return
    if y==0:
        print(2)
        return
    if y==1:
        print(x-1)
        return
    if y==2:
        print(x)
        return
    if x==3 and y==3:
        print(2)
        return
    if y>=4:
        print((x+y-2)%1000000007)
        return
    if x==4 and y==3:
        print(4)
        return
    if x==4 and y==4:
        print(4)
        return
    if x==5 and y==3:
        print(4)
        return
    if x==5 and y==4:
        print(8)
        return
    if x==5 and y==5:
        print(4)
        return
    if x==6 and y==3:
        print(4)
        return
    if x==6 and y==4:
        print(8)
        return
    if x==6 and y==5:
        print(8)
        return
    if x==6 and y==6:
        print(4)
        return
    if x==7 and y==3:
        print(4)
        return
    if x==7 and y==4:
        print(8)
        return
    if x==7 and y==5:
        print(12)
        return
    if x==7 and y==6:
        print(8)
        return
    if x==7 and y==7:
        print(4)
        return
    if x==8 and y==3:
        print(4)
        return
    if x==8 and y==4:
        print(8)
        return
    if x==8 and y==5:
        print(12)
        return
    if x==8 and y==6:
        print(16)

=======
Suggestion 4

def solve(x, y):
    mod = 10 ** 9 + 7
    dp = [[0] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = 1
    for i in range(x + 1):
        for j in range(y + 1):
            if i + 1 <= x and j + 2 <= y:
                dp[i + 1][j + 2] += dp[i][j]
                dp[i + 1][j + 2] %= mod
            if i + 2 <= x and j + 1 <= y:
                dp[i + 2][j + 1] += dp[i][j]
                dp[i + 2][j + 1] %= mod
    return dp[x][y]

=======
Suggestion 5

def main():
    #输入
    x,y = map(int,input().split())
    #求解
    ans = 0
    if (x+y)%3 == 0:
        if x<=y*2 and y<=x*2:
            ans = 1
            for i in range(1,x):
                ans = ans*(x+y-i)%1000000007
                ans = ans*pow(i,1000000005,1000000007)%1000000007
    #输出
    print(ans)

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    MOD = 10**9+7
    dp = [[0]*(Y+1) for _ in range(X+1)]
    dp[0][0] = 1
    for i in range(X+1):
        for j in range(Y+1):
            if i+1 <= X and j+2 <= Y:
                dp[i+1][j+2] += dp[i][j]
                dp[i+1][j+2] %= MOD
            if i+2 <= X and j+1 <= Y:
                dp[i+2][j+1] += dp[i][j]
                dp[i+2][j+1] %= MOD
    print(dp[X][Y])

=======
Suggestion 7

def solve(x, y):
    # 1. 构造二维数组
    # 2. 初始化数组
    # 3. 递推
    # 4. 返回结果
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(x+1):
        for j in range(y+1):
            if i+1 <= x and j+2 <= y:
                dp[i+1][j+2] = (dp[i+1][j+2] + dp[i][j]) % (10**9+7)
            if i+2 <= x and j+1 <= y:
                dp[i+2][j+1] = (dp[i+2][j+1] + dp[i][j]) % (10**9+7)
    return dp[x][y]

=======
Suggestion 8

def solve(x, y):
    MOD = 10**9 + 7
    if (x + y) % 3 != 0:
        return 0
    n = (x + y) // 3
    x = x - n
    y = y - n
    if x < 0 or y < 0:
        return 0
    return combination(n, x, MOD)

=======
Suggestion 9

def knight(x,y):
    if x==0 and y==0:
        return 1
    elif x<0 or y<0:
        return 0
    else:
        return (knight(x-2,y-1)+knight(x-1,y-2))%1000000007

=======
Suggestion 10

def main():
    X, Y = map(int, input().split())
    mod = 10**9 + 7

    if (X + Y) % 3 != 0:
        print(0)
        return

    n = (2 * Y - X) // 3
    m = (2 * X - Y) // 3

    if n < 0 or m < 0:
        print(0)
        return

    N = n + m
    M = min(n, m)

    fac = [1] * (N + 1)
    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i % mod

    inv = [1] * (N + 1)
    inv[N] = pow(fac[N], mod - 2, mod)
    for i in range(N - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % mod

    print(fac[N] * inv[M] * inv[N - M] % mod)
