Synthesizing 9/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    print((N*(N-1))//2)

=======
Suggestion 2

def main():
    N = int(input())
    print(N*(N-1)//2)

=======
Suggestion 3

def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n == 4:
        return 6
    if n == 5:
        return 10
    if n == 6:
        return 15
    if n == 7:
        return 21
    if n == 8:
        return 28
    if n == 9:
        return 36
    if n == 10:
        return 45
    if n == 11:
        return 55
    if n == 12:
        return 66
    if n == 13:
        return 78
    if n == 14:
        return 91
    if n == 15:
        return 105
    if n == 16:
        return 120
    if n == 17:
        return 136
    if n == 18:
        return 153
    if n == 19:
        return 171
    if n == 20:
        return 190
    if n == 21:
        return 210
    if n == 22:
        return 231
    if n == 23:
        return 253
    if n == 24:
        return 276
    if n == 25:
        return 300
    if n == 26:
        return 325
    if n == 27:
        return 351
    if n == 28:
        return 378
    if n == 29:
        return 406
    if n == 30:
        return 435
    if n == 31:
        return 465
    if n == 32:
        return 496
    if n == 33:
        return 528
    if n == 34:
        return 561
    if n == 35:
        return 595
    if n == 36:
        return 630
    if n == 37:
        return 666
    if n == 38:
        return 703
    if n == 39:
        return 741
    if n == 40:
        return 780
    if n == 41:
        return 820
    if n ==

=======
Suggestion 4

def get_max_p(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return n * (n - 1) // 2
    else:
        return (n - 1) * (n - 2) // 2 + n - 1

=======
Suggestion 5

def main():
    N = int(input())
    print(N*(N-1)//2)
main()

=======
Suggestion 6

def solve(n):
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(2)
    elif n%2 == 0:
        print(n*(n-1)//2)
    else:
        print(n*(n-1)//2 - 1)

=======
Suggestion 7

def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return n * (n - 1) // 2
    else:
        return n * (n - 1) // 2 + (n - 1) // 2

=======
Suggestion 8

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N*(N-1)//2)

=======
Suggestion 9

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(int(n * (n - 1) / 2))
