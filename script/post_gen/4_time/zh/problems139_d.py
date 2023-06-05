Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_sum(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return n * (n - 1) / 2
    else:
        return (n - 1) * (n - 2) / 2 + n

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += N // i
    if N % i == 0:
        ans -= 1
print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    elif N == 3:
        print(3)
    elif N == 4:
        print(6)
    elif N == 5:
        print(10)
    elif N == 6:
        print(15)
    elif N == 7:
        print(21)
    elif N == 8:
        print(28)
    elif N == 9:
        print(36)
    elif N == 10:
        print(45)
    elif N == 11:
        print(55)
    elif N == 12:
        print(66)
    elif N == 13:
        print(78)
    elif N == 14:
        print(91)
    elif N == 15:
        print(105)
    elif N == 16:
        print(120)
    elif N == 17:
        print(136)
    elif N == 18:
        print(153)
    elif N == 19:
        print(171)
    elif N == 20:
        print(190)
    elif N == 21:
        print(210)
    elif N == 22:
        print(231)
    elif N == 23:
        print(253)
    elif N == 24:
        print(276)
    elif N == 25:
        print(300)
    elif N == 26:
        print(325)
    elif N == 27:
        print(351)
    elif N == 28:
        print(378)
    elif N == 29:
        print(406)
    elif N == 30:
        print(435)
    elif N == 31:
        print(465)
    elif N == 32:
        print(496)
    elif N == 33:
        print(528)
    elif N == 34:
        print(561)
    elif N == 35:
        print(595)
    elif N == 36:
        print(630)
    elif N == 37:
        print(666)
    elif N == 38:
        print(703)
    elif N == 39:
        print(741)
    elif N == 40:
        print(780)
    elif N == 41:
        print(820)

=======
Suggestion 4

def main():
    n = int(input())
    print(n*(n-1)//2)

=======
Suggestion 5

def p139(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 3
    elif n == 4:
        return 4
    elif n == 5:
        return 10
    elif n == 6:
        return 15
    elif n == 7:
        return 21
    elif n == 8:
        return 28
    elif n == 9:
        return 36
    elif n == 10:
        return 45
    elif n == 11:
        return 55
    elif n == 12:
        return 66
    elif n == 13:
        return 78
    elif n == 14:
        return 91
    elif n == 15:
        return 105
    elif n == 16:
        return 120
    elif n == 17:
        return 136
    elif n == 18:
        return 153
    elif n == 19:
        return 171
    elif n == 20:
        return 190
    elif n == 21:
        return 210
    elif n == 22:
        return 231
    elif n == 23:
        return 253
    elif n == 24:
        return 276
    elif n == 25:
        return 300
    elif n == 26:
        return 325
    elif n == 27:
        return 351
    elif n == 28:
        return 378
    elif n == 29:
        return 406
    elif n == 30:
        return 435
    elif n == 31:
        return 465
    elif n == 32:
        return 496
    elif n == 33:
        return 528
    elif n == 34:
        return 561
    elif n == 35:
        return 595
    elif n == 36:
        return 630
    elif n == 37:
        return 666
    elif n == 38:
        return 703
    elif n == 39:
        return 741
    elif n == 40:
        return 780
    elif n == 41:
        return 820
    elif n ==

=======
Suggestion 6

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(int(n*(n-1)/2))

=======
Suggestion 7

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        sum += i
    print(sum)

=======
Suggestion 8

def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return n * (n - 1) // 2
    else:
        return (n - 1) * (n - 2) // 2 + n

=======
Suggestion 9

def solve(n):
    n = int(n)
    res = 0
    for i in range(1, n + 1):
        res += n // i * i
    return res

=======
Suggestion 10

def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 3
    elif n == 4:
        return 6
    elif n == 5:
        return 10
    elif n == 6:
        return 15
    elif n == 7:
        return 21
    elif n == 8:
        return 28
    elif n == 9:
        return 36
    elif n == 10:
        return 45
    elif n == 11:
        return 55
    elif n == 12:
        return 66
    elif n == 13:
        return 78
    elif n == 14:
        return 91
    elif n == 15:
        return 105
    elif n == 16:
        return 120
    elif n == 17:
        return 136
    elif n == 18:
        return 153
    elif n == 19:
        return 171
    elif n == 20:
        return 190
    elif n == 21:
        return 210
    elif n == 22:
        return 231
    elif n == 23:
        return 253
    elif n == 24:
        return 276
    elif n == 25:
        return 300
    elif n == 26:
        return 325
    elif n == 27:
        return 351
    elif n == 28:
        return 378
    elif n == 29:
        return 406
    elif n == 30:
        return 435
    elif n == 31:
        return 465
    elif n == 32:
        return 496
    elif n == 33:
        return 528
    elif n == 34:
        return 561
    elif n == 35:
        return 595
    elif n == 36:
        return 630
    elif n == 37:
        return 666
    elif n == 38:
        return 703
    elif n == 39:
        return 741
    elif n == 40:
        return 780
    elif n == 41:
        return 820
    elif n ==
