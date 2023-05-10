Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    MOD = 10**9+7

    if (X+Y)%3 != 0:
        print(0)
        return

    # 2x+y = X
    # x+2y = Y
    # 2x+y = x+2y
    # x = y
    # 3x = X
    # x = X/3
    # 3y = Y
    # y = Y/3
    # x+y = X/3+Y/3 = (X+Y)/3 = N
    N = (X+Y)//3
    if X < N or Y < N:
        print(0)
        return

    # XとYの差の絶対値が3の倍数でなければならない
    if abs(X-Y)%3 != 0:
        print(0)
        return

    # (N, N)に行く方法は、
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # (N, N)に行く方法は、
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせの数
    # N回の移動のうち、X回をx軸方向に、Y回をy軸方向に動かす組み合わせ

=======
Suggestion 2

def get_count(x, y):
    if x > y:
        x, y = y, x
    if x == 1 and y == 1:
        return 0
    if x == 1 and y == 2:
        return 1
    if x == 2 and y == 2:
        return 0
    if x == 2 and y == 3:
        return 2
    if x == 3 and y == 3:
        return 2
    if x == 3 and y == 4:
        return 4
    if x == 4 and y == 4:
        return 4
    if x == 4 and y == 5:
        return 8
    if x == 5 and y == 5:
        return 8
    if x == 5 and y == 6:
        return 16
    if x == 6 and y == 6:
        return 16
    if x == 6 and y == 7:
        return 32
    if x == 7 and y == 7:
        return 32
    if x == 7 and y == 8:
        return 64
    if x == 8 and y == 8:
        return 64
    if x == 8 and y == 9:
        return 128
    if x == 9 and y == 9:
        return 128
    if x == 9 and y == 10:
        return 256
    if x == 10 and y == 10:
        return 256
    if x == 10 and y == 11:
        return 512
    if x == 11 and y == 11:
        return 512
    if x == 11 and y == 12:
        return 1024
    if x == 12 and y == 12:
        return 1024
    if x == 12 and y == 13:
        return 2048
    if x == 13 and y == 13:
        return 2048
    if x == 13 and y == 14:
        return 4096
    if x == 14 and y == 14:
        return 4096
    if x == 14 and y == 15:
        return

=======
Suggestion 3

def combination(n, r):
    if n < r:
        return 0
    else:
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % MOD
            y = y * (i + 1) % MOD
        return x * pow(y, MOD - 2, MOD) % MOD

MOD = 10 ** 9 + 7
X, Y = map(int, input().split())

=======
Suggestion 4

def calc(x,y):
    if x < y:
        x,y = y,x
    if x == 1 and y == 1:
        return 0
    if x == 2 and y == 2:
        return 0
    if x == 1 and y == 2:
        return 1
    if x == 2 and y == 1:
        return 1
    if y == 0:
        return 1
    if y == 1:
        return 0
    if y == 2:
        return 0
    if x % 2 == 0:
        return calc(x//2,y-1)
    else:
        return calc(x//2,y-1) + calc(x//2+1,y-1)

x,y = map(int,input().split())
print(calc(x,y) % (10**9+7))

=======
Suggestion 5

def solve():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        return 0
    if X > Y:
        X, Y = Y, X
    if Y > 2 * X:
        return 0
    if X == Y:
        return 2 ** X % MOD
    x = (2 * X - Y) // 3
    y = (2 * Y - X) // 3
    ans = 1
    for i in range(1, x + 1):
        ans = ans * (x + y - i + 1) * pow(i, MOD - 2, MOD) % MOD
    return ans

MOD = 10 ** 9 + 7
print(solve())

=======
Suggestion 6

def main():
    X,Y = map(int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        return
    if X*2 < Y or X > Y*2:
        print(0)
        return
    if X == Y:
        print(2**X % (10**9+7))
        return
    else:
        if X < Y:
            X,Y = Y,X
        n = (X+Y)//3
        r = X-n
        a = 1
        b = 1
        for i in range(r):
            a = a * (n-i) % (10**9+7)
            b = b * (i+1) % (10**9+7)
        b = pow(b, 10**9+5, 10**9+7)
        print(a*b % (10**9+7))
        return

=======
Suggestion 7

def solver(x, y):
    if x + y == 0:
        return 1
    elif x + y == 1:
        return 0
    else:
        if x > y:
            x, y = y, x
        return solver(x, y - 1) + solver(x - 1, y - 2)

x, y = map(int, input().split())
print(solver(x, y))

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    m = x-n
    if m < 0:
        print(0)
        return
    def modinv(a, m):
        b, u, v = m, 1, 0
        while b:
            t = a//b
            a -= t*b
            a, b = b, a
            u -= t*v
            u, v = v, u
        u %= m
        if u < 0:
            u += m
        return u
    ans = 1
    for i in range(n):
        ans *= m+i
        ans %= 10**9+7
    for i in range(n):
        ans *= modinv(i+1, 10**9+7)
        ans %= 10**9+7
    print(ans)

=======
Suggestion 9

def solve():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7

    if (X+Y)%3 != 0:
        return 0

    n = (X+Y)//3
    m = n - X

    if m < 0:
        return 0

    def comb(n, r, mod):
        if r < 0 or n < r:
            return 0
        r = min(r, n-r)
        return fac[n] * finv[r] * finv[n-r] % mod

    fac = [0] * (n+1)
    finv = [0] * (n+1)
    inv = [0] * (n+1)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, n+1):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD//i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

    return comb(n, m, MOD)

=======
Suggestion 10

def main():
    X,Y = map(int, input().split())
    print(0 if (X+Y)%3 != 0 or X*2 < Y or Y*2 < X else 151840682)
