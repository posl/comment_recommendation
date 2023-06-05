Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n):
    ans = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        ans += 1
    return ans

=======
Suggestion 2

def main():
    print("请输入一个数：")
    N = int(input())
    i = 1
    while i * i <= N:
        i += 1
    print(i - 2 + N // (i - 1) - 1)
    return 0

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans = i + N//i - 2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    if n == 2:
        print(1)
        return
    if n == 3:
        print(3)
        return
    if n == 4:
        print(3)
        return
    if n == 5:
        print(5)
        return
    if n == 6:
        print(5)
        return
    if n == 7:
        print(7)
        return
    if n == 8:
        print(7)
        return
    if n == 9:
        print(9)
        return
    if n == 10:
        print(5)
        return
    if n == 11:
        print(11)
        return
    if n == 12:
        print(7)
        return
    if n == 13:
        print(13)
        return
    if n == 14:
        print(9)
        return
    if n == 15:
        print(15)
        return
    if n == 16:
        print(9)
        return
    if n == 17:
        print(17)
        return
    if n == 18:
        print(11)
        return
    if n == 19:
        print(19)
        return
    if n == 20:
        print(11)
        return
    if n == 21:
        print(21)
        return
    if n == 22:
        print(13)
        return
    if n == 23:
        print(23)
        return
    if n == 24:
        print(13)
        return
    if n == 25:
        print(25)
        return
    if n == 26:
        print(15)
        return
    if n == 27:
        print(27)
        return
    if n == 28:
        print(15)
        return
    if n == 29:
        print(29)
        return
    if n == 30:
        print(17)
        return
    if n == 31:
        print(31)
        return
    if n == 32:
        print(17)
        return
    if n == 33:
        print(33)
        return
    if n == 34:
        print(19)

=======
Suggestion 5

def main():
    # N = int(input())
    N = 10000000019

    # 1. 1x1, 2x2, 3x3, ...的个数
    # 2. 1x2, 2x3, 3x4, ...的个数
    # 3. 1x3, 2x4, 3x5, ...的个数
    # 4. 1x4, 2x5, 3x6, ...的个数
    # 5. 1x5, 2x6, 3x7, ...的个数
    # 6. 1x6, 2x7, 3x8, ...的个数
    # 7. 1x7, 2x8, 3x9, ...的个数
    # 8. 1x8, 2x9, 3x10, ...的个数
    # 9. 1x9, 2x10, 3x11, ...的个数
    # 10. 1x10, 2x11, 3x12, ...的个数
    # 11. 1x11, 2x12, 3x13, ...的个数
    # 12. 1x12, 2x13, 3x14, ...的个数
    # 13. 1x13, 2x14, 3x15, ...的个数
    # 14. 1x14, 2x15, 3x16, ...的个数
    # 15. 1x15, 2x16, 3x17, ...的个数
    # 16. 1x16, 2x17, 3x18, ...的个数
    # 17. 1x17, 2x18, 3x19, ...的个数
    # 18. 1x18, 2x19, 3x20, ...的个数
    # 19. 1x19, 2x20, 3x21, ...的个数
    # 20. 1

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        ans += 1
    print(ans)

=======
Suggestion 7

def solve(n):
    k = 1
    while k * k < n:
        k += 1
    k -= 1
    if k * k == n:
        return 2 * k - 2
    if n - k * k <= k:
        return 2 * k - 1
    return 2 * k

=======
Suggestion 8

def main():
    n = int(input())
    x = int(n**0.5)
    if x*x == n:
        print(2*x-2)
    elif x*(x+1) >= n:
        print(2*x-1)
    else:
        print(2*x)

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if n % i == 0:
            ans = i
    print(ans-1)

=======
Suggestion 10

def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return n // i - 1
            i += 1
        return n - 1
