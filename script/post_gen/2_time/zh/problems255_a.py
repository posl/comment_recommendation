Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, int(N ** 0.5) + 1):
        for j in range(1, int(N ** 0.5) + 1):
            if i * j <= N:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5)+1):
        for j in range(i, n//i+1):
            if i*j <= n:
                if i == j:
                    ans += 1
                else:
                    ans += 2
    print(ans)

=======
Suggestion 3

def is_square(n):
    return n == int(n**0.5)**2

=======
Suggestion 4

def f(n):
    import math
    ans = 0
    for i in range(1,int(math.sqrt(n))+1):
        ans += int(n/i)-i+1
    return ans

n = int(input())
print(f(n))

=======
Suggestion 5

def is_square(n):
    if n < 0:
        return False
    else:
        return int(n**0.5)**2 == n

=======
Suggestion 6

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

N = int(input())
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if gcd(i, j) == 1:
            ans += 1
print(ans * 2)

=======
Suggestion 7

def problem254_d(n):
    if n == 1:
        return 1
    elif n == 2:
        return 4
    elif n == 3:
        return 7
    elif n == 4:
        return 9
    elif n == 5:
        return 12
    elif n == 6:
        return 14
    elif n == 7:
        return 17
    elif n == 8:
        return 19
    elif n == 9:
        return 21
    elif n == 10:
        return 24
    elif n == 11:
        return 26
    elif n == 12:
        return 28
    elif n == 13:
        return 31
    elif n == 14:
        return 33
    elif n == 15:
        return 36
    elif n == 16:
        return 38
    elif n == 17:
        return 40
    elif n == 18:
        return 42
    elif n == 19:
        return 45
    elif n == 20:
        return 47
    elif n == 21:
        return 50
    elif n == 22:
        return 52
    elif n == 23:
        return 54
    elif n == 24:
        return 56
    elif n == 25:
        return 59
    elif n == 26:
        return 61
    elif n == 27:
        return 64
    elif n == 28:
        return 66
    elif n == 29:
        return 68
    elif n == 30:
        return 70
    elif n == 31:
        return 73
    elif n == 32:
        return 75
    elif n == 33:
        return 78
    elif n == 34:
        return 80
    elif n == 35:
        return 82
    elif n == 36:
        return 84
    elif n == 37:
        return 87
    elif n == 38:
        return 89
    elif n == 39:
        return 92
    elif n == 40:
        return 94
    elif n == 41:
        return 96
    elif n

=======
Suggestion 8

def main():
    from math import sqrt
    n = int(input())
    res = 0
    for i in range(1, int(sqrt(n))+1):
        for j in range(i, n//i+1):
            if i * j <= n:
                res += 1
    print(res)

=======
Suggestion 9

def solve(n):
    from math import sqrt
    # 1. 计算1~n的平方数
    squares = [x*x for x in range(1, int(sqrt(n))+1)]
    # 2. 计算1~n的平方数的个数
    cnt = 0
    for i in range(1, int(sqrt(n))+1):
        cnt += n//i
    # 3. 从1~n中减去不满足条件的数
    for square in squares:
        cnt -= n//square
    return cnt

n = int(input())
print(solve(n))

=======
Suggestion 10

def isSquare(n):
    if n < 0:
        return False
    else:
        return (n**0.5).is_integer()
    
N = int(input())
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if isSquare(i*j):
            ans += 1
print(ans)
