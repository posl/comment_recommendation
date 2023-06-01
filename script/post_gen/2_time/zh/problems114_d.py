Synthesizing 9/10 solutions

=======
Suggestion 1

def calc753(N):
    if N < 3:
        return 0
    if N < 5:
        return 1
    if N < 7:
        return 2
    if N < 35:
        return 3
    if N < 37:
        return 4
    if N < 53:
        return 5
    if N < 57:
        return 6
    if N < 73:
        return 7
    if N < 75:
        return 8
    if N < 77:
        return 9
    if N < 335:
        return 10
    if N < 337:
        return 11
    if N < 353:
        return 12
    if N < 355:
        return 13
    if N < 357:
        return 14
    if N < 373:
        return 15
    if N < 375:
        return 16
    if N < 377:
        return 17
    if N < 533:
        return 18
    if N < 535:
        return 19
    if N < 537:
        return 20
    if N < 553:
        return 21
    if N < 555:
        return 22
    if N < 557:
        return 23
    if N < 573:
        return 24
    if N < 575:
        return 25
    if N < 577:
        return 26
    if N < 733:
        return 27
    if N < 735:
        return 28
    if N < 737:
        return 29
    if N < 753:
        return 30
    if N < 755:
        return 31
    if N < 757:
        return 32
    if N < 773:
        return 33
    if N < 775:
        return 34
    if N < 777:
        return 35
    if N < 3335:
        return 36
    if N < 3337:
        return 37
    if N < 3353:
        return 38
    if N < 3355:
        return 39
    if N < 3357:
        return 40

=======
Suggestion 2

def is753(n):
    s = str(n)
    return s.count('7') and s.count('5') and s.count('3')

=======
Suggestion 3

def is753(num):
    if num % 10 == 7:
        return True
    elif num % 10 == 5:
        return True
    elif num % 10 == 3:
        return True
    else:
        return False

=======
Suggestion 4

def is753(n):
    n = str(n)
    if '7' in n and '5' in n and '3' in n:
        return True
    else:
        return False

=======
Suggestion 5

def is753(num):
    if num < 357:
        return False
    if num % 2 == 0:
        return False
    if num % 5 == 0:
        return False
    if num % 7 == 0:
        return False
    if num % 3 != 0:
        return False

    return True

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '3' in str(i) and '5' in str(i) and '7' in str(i):
            count += 1
    print(count)

=======
Suggestion 7

def is753(num):
    num = str(num)
    if '7' in num and '5' in num and '3' in num:
        return True
    else:
        return False

=======
Suggestion 8

def check753(num):
    num = str(num)
    if '7' in num and '5' in num and '3' in num:
        return True
    return False

=======
Suggestion 9

def is753(n):
    if n % 10 == 3 or n % 10 == 5 or n % 10 == 7:
        return True
    elif n >= 10:
        return is753(n // 10)
    else:
        return False
