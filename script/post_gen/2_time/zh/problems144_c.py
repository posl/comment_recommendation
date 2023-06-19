Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def solve(n):
    # 1 <= n <= 10^12
    # 1 <= i, j <= 10^6
    # 1 <= i * j <= 10^12
    # 1 <= i + j <= 2 * 10^6
    # 1 <= i + j + 1 <= 2 * 10^6
    # 1 <= i + j + 2 <= 2 * 10^6
    # 1 <= i + j + 3 <= 2 * 10^6
    # 1 <= i + j + 4 <= 2 * 10^6
    # 1 <= i + j + 5 <= 2 * 10^6
    # 1 <= i + j + 6 <= 2 * 10^6
    # 1 <= i + j + 7 <= 2 * 10^6
    # 1 <= i + j + 8 <= 2 * 10^6
    # 1 <= i + j + 9 <= 2 * 10^6
    # 1 <= i + j + 10 <= 2 * 10^6
    # 1 <= i + j + 11 <= 2 * 10^6
    # 1 <= i + j + 12 <= 2 * 10^6
    # 1 <= i + j + 13 <= 2 * 10^6
    # 1 <= i + j + 14 <= 2 * 10^6
    # 1 <= i + j + 15 <= 2 * 10^6
    # 1 <= i + j + 16 <= 2 * 10^6
    # 1 <= i + j + 17 <= 2 * 10^6
    # 1 <= i + j + 18 <= 2 * 10^6
    # 1 <= i + j + 19 <= 2 * 10^6
    # 1 <= i + j + 20 <= 2 * 10^6
    # 1 <= i + j + 21 <= 2 * 10^6
    # 1 <= i + j + 22 <= 2 * 10^6

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 1:
            N -= 1
        else:
            N /= 2
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    print(N-1)
    return

=======
Suggestion 5

def main():
    n = int(input())
    if n==2:
        print(1)
        return
    if n==3:
        print(2)
        return
    if n==4:
        print(2)
        return
    if n==5:
        print(3)
        return
    if n==6:
        print(3)
        return
    if n==7:
        print(4)
        return
    if n==8:
        print(4)
        return
    if n==9:
        print(5)
        return
    if n==10:
        print(5)
        return
    if n==11:
        print(6)
        return
    if n==12:
        print(6)
        return
    if n==13:
        print(7)
        return
    if n==14:
        print(7)
        return
    if n==15:
        print(8)
        return
    if n==16:
        print(8)
        return
    if n==17:
        print(9)
        return
    if n==18:
        print(9)
        return
    if n==19:
        print(10)
        return
    if n==20:
        print(10)
        return
    if n==21:
        print(11)
        return
    if n==22:
        print(11)
        return
    if n==23:
        print(12)
        return
    if n==24:
        print(12)
        return
    if n==25:
        print(13)
        return
    if n==26:
        print(13)
        return
    if n==27:
        print(14)
        return
    if n==28:
        print(14)
        return
    if n==29:
        print(15)
        return
    if n==30:
        print(15)
        return
    if n==31:
        print(16)
        return
    if n==32:
        print(16)
        return
    if n==33:
        print(17)
        return
    if n==34:
        print(17)
        return
    if n==35:
        print(18)
        return
    if n==36:
        print(18)
        return
    if

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    x = 1
    while x * x <= n:
        if n % x == 0:
            ans = max(ans, x)
            ans = max(ans, n // x)
        x += 1
    print(ans - 2)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            ans = max(ans, i)
            while n % i == 0:
                n //= i
    if n != 1:
        ans = max(ans, n)
    print(ans-1 if ans else 0)

=======
Suggestion 8

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i*i > n:
            break
        if n % i == 0:
            count += 1
    print(count*2)

=======
Suggestion 9

def main():
    n = int(input())
    ans = n - 1
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans = min(ans, i + n // i - 2)
    print(ans)
main()

=======
Suggestion 10

def main():
    n = int(input())
    i = 1
    while i*i <= n:
        i += 1
    print(i-1)
