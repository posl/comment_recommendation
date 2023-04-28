Synthesizing 10/10 solutions

=======
Suggestion 1

def is753(n):
    s = str(n)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0 and s.count('4') == 0 and s.count('6') == 0 and s.count('8') == 0 and s.count('9') == 0

n = int(input())
cnt = 0
for i in range(1, n + 1):
    if is753(i):
        cnt += 1
print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    cnt = 0
    for i in range(3,n+1):
        if '3' in str(i) and '5' in str(i) and '7' in str(i):
            cnt += 1
    print(cnt)

=======
Suggestion 3

def solve():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                if i == 3 and j == 5 and k == 7:
                    ans += 1
                elif i == 3 and j == 7 and k == 5:
                    ans += 1
                elif i == 5 and j == 3 and k == 7:
                    ans += 1
                elif i == 5 and j == 7 and k == 3:
                    ans += 1
                elif i == 7 and j == 3 and k == 5:
                    ans += 1
                elif i == 7 and j == 5 and k == 3:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                for l in range(3, 10):
                    for m in range(3, 10):
                        for n in range(3, 10):
                            for o in range(3, 10):
                                for p in range(3, 10):
                                    num = 10000000 * i + 1000000 * j + 100000 * k + 10000 * l + 1000 * m + 100 * n + 10 * o + p
                                    if num <= N and (i == 7 or j == 7 or k == 7 or l == 7 or m == 7 or n == 7 or o == 7 or p == 7) and (i == 5 or j == 5 or k == 5 or l == 5 or m == 5 or n == 5 or o == 5 or p == 5) and (i == 3 or j == 3 or k == 3 or l == 3 or m == 3 or n == 3 or o == 3 or p == 3):
                                        ans += 1
    print(ans)
main()

=======
Suggestion 5

def is753(n):
    if n == 0:
        return True
    if n % 10 == 7 or n % 10 == 5 or n % 10 == 3:
        return is753(n // 10)
    else:
        return False

=======
Suggestion 6

def count753(n):
    if n < 10:
        if n == 7 or n == 5 or n == 3:
            return 1
        else:
            return 0
    else:
        a = n % 10
        b = n // 10
        return count753(a) + count753(b)

N = int(input())
print(count753(N))

=======
Suggestion 7

def is753(n):
    if n < 100:
        return False
    else:
        s = str(n)
        if '7' in s and '5' in s and '3' in s:
            return True
        else:
            return False

=======
Suggestion 8

def is753(n):
    if n < 10:
        return (n == 3) or (n == 5) or (n == 7)
    else:
        return is753(n % 10) and is753(n // 10)

=======
Suggestion 9

def is753(n):
    if n < 357:
        return False
    if n % 10 == 7 or n % 10 == 5 or n % 10 == 3:
        if n // 10 == 0:
            return True
        else:
            return is753(n // 10)
    else:
        return False

=======
Suggestion 10

def seven_five_three(num):
    if num > 1000000000:
        return 0
    if num < 357:
        return 0
    if num < 375:
        return 1
    if num < 537:
        return 2
    if num < 573:
        return 3
    if num < 735:
        return 4
    if num < 753:
        return 5
    if num < 3357:
        return 6
    if num < 3375:
        return 7
    if num < 3537:
        return 8
    if num < 3557:
        return 9
    if num < 3573:
        return 10
    if num < 3575:
        return 11
    if num < 3577:
        return 12
    return 13
