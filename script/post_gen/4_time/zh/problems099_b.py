Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_snow(a,b):
    return b-a-1

=======
Suggestion 2

def getSnowDepth(a, b):
    if a == 1:
        return 1
    if a == 2:
        return 2
    if a == 3:
        return 2
    if a == 4:
        return 3
    if a == 5:
        return 3
    if a == 6:
        return 3
    if a == 7:
        return 4
    if a == 8:
        return 4
    if a == 9:
        return 4
    if a == 10:
        return 4
    if a == 11:
        return 5
    if a == 12:
        return 5
    if a == 13:
        return 5
    if a == 14:
        return 5
    if a == 15:
        return 5
    if a == 16:
        return 6
    if a == 17:
        return 6
    if a == 18:
        return 6
    if a == 19:
        return 6
    if a == 20:
        return 6
    if a == 21:
        return 6
    if a == 22:
        return 7
    if a == 23:
        return 7
    if a == 24:
        return 7
    if a == 25:
        return 7
    if a == 26:
        return 7
    if a == 27:
        return 7
    if a == 28:
        return 7
    if a == 29:
        return 8
    if a == 30:
        return 8
    if a == 31:
        return 8
    if a == 32:
        return 8
    if a == 33:
        return 8
    if a == 34:
        return 8
    if a == 35:
        return 8
    if a == 36:
        return 8
    if a == 37:
        return 9
    if a == 38:
        return 9
    if a == 39:
        return 9
    if a == 40:
        return 9
    if a == 41:
        return 9

=======
Suggestion 3

def snow(a,b):
    n = b - a
    x = 1
    while True:
        if n > x:
            x += 1
            n -= x
        else:
            break
    return x

=======
Suggestion 4

def solution(a,b):
    #a,b = map(int,input().split())
    #print(a,b)
    #print(b-a)
    return b-a-1

=======
Suggestion 5

def solve():
    a, b = map(int, input().split())
    print(b - a - 1)

=======
Suggestion 6

def problem099_b():
    pass

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    h = b - a
    print(int(h * (h - 1) / 2 - a))

=======
Suggestion 8

def get_snow_height(a, b):
    # 1+2+3+...+n = n(n+1)/2
    # 1+2+3+...+n-1 = (n-1)n/2
    # 1+2+3+...+n-(1+2+3+...+n-1) = n
    # 1+2+3+...+n-(1+2+3+...+n-1) = n(n+1)/2 - (n-1)n/2 = n
    # 1+2+3+...+n-(1+2+3+...+n-1) = n(n+1-n+1)/2 = n
    # n = 1+2+3+...+n-(1+2+3+...+n-1)
    # n = b - a
    # b - a = 1+2+3+...+n-(1+2+3+...+n-1)
    # b - a = n
    # n = b - a
    # 1+2+3+...+n-(1+2+3+...+n-1) = n
    # 1+2+3+...+n-(1+2+3+...+n-1) = b - a
    # 1+2+3+...+n-(1+2+3+...+n-1) = 1+2+3+...+n-(1+2+3+...+n-1)
    # 1+2+3+...+n-(1+2+3+...+n-1) = 1+2+3+...+n-(1+2+3+...+n-1)
    # 1+2+3+...+n-(1+2+3+...+n-1) = 1+2+3+...+n-(1+2+3+...+n-1)
    # 1+2+3+...+n-(1+2+3+...+n-1) = 1+2+3+...+n-(1+2+3+...+n-1)
    # 1+2

=======
Suggestion 9

def get_hight(a,b):
    if a >= b:
        return -1

    sum = 0
    for i in range(1,1000):
        sum = sum + i
        if sum >= a:
            break

    if sum != a:
        return -1

    sum = 0
    for i in range(1,1000):
        sum = sum + i
        if sum >= b:
            break

    if sum != b:
        return -1

    return b - a
