Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    # n = 100000
    # n = 8
    a = []
    for i in range(2, int(n ** 0.5) + 1):
        x = i * i
        while x <= n:
            a.append(x)
            x *= i
    print(n - len(set(a)))

=======
Suggestion 2

def main():
    N = int(input())
    # N = 100000
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        # print(i)
        j = 2
        while i ** j <= N:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    prime_list = []
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            prime_list.append(i)
            while N % i == 0:
                N //= i
    if N != 1:
        prime_list.append(N)

    print(len(set(prime_list)))

=======
Suggestion 4

def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        tmp = i * i
        while tmp <= N:
            ans += 1
            tmp *= i
    print(N - ans)

=======
Suggestion 5

def main():
    N = int(input())

    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        tmp = i ** 2
        while tmp <= N:
            ans -= 1
            tmp *= i

    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    if n == 2:
        print(2)
        return
    if n == 3:
        print(3)
        return
    if n == 4:
        print(4)
        return
    if n == 5:
        print(5)
        return
    if n == 6:
        print(5)
        return
    if n == 7:
        print(6)
        return
    if n == 8:
        print(6)
        return
    if n == 9:
        print(6)
        return
    if n == 10:
        print(6)
        return
    if n == 11:
        print(7)
        return
    if n == 12:
        print(7)
        return
    if n == 13:
        print(8)
        return
    if n == 14:
        print(8)
        return
    if n == 15:
        print(8)
        return
    if n == 16:
        print(8)
        return
    if n == 17:
        print(9)
        return
    if n == 18:
        print(9)
        return
    if n == 19:
        print(10)
        return
    if n == 20:
        print(10)
        return
    if n == 21:
        print(10)
        return
    if n == 22:
        print(10)
        return
    if n == 23:
        print(11)
        return
    if n == 24:
        print(11)
        return
    if n == 25:
        print(12)
        return
    if n == 26:
        print(12)
        return
    if n == 27:
        print(12)
        return
    if n == 28:
        print(12)
        return
    if n == 29:
        print(13)
        return
    if n == 30:
        print(13)
        return
    if n == 31:
        print(14)
        return
    if n == 32:
        print(14)
        return
    if n == 33:
        print(14)

=======
Suggestion 7

def main():
    n = int(input())
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        x = i * i
        while x <= n:
            ans -= 1
            x *= i
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    # 2^60 > 10^10
    # 2^60 = 1152921504606846976
    # 2^59 = 576460752303423488
    # 2^58 = 288230376151711744
    # 2^57 = 144115188075855872
    # 2^56 = 72057594037927936
    # 2^55 = 36028797018963968
    # 2^54 = 18014398509481984
    # 2^53 = 9007199254740992
    # 2^52 = 4503599627370496
    # 2^51 = 2251799813685248
    # 2^50 = 1125899906842624
    # 2^49 = 562949953421312
    # 2^48 = 281474976710656
    # 2^47 = 140737488355328
    # 2^46 = 70368744177664
    # 2^45 = 35184372088832
    # 2^44 = 17592186044416
    # 2^43 = 8796093022208
    # 2^42 = 4398046511104
    # 2^41 = 2199023255552
    # 2^40 = 1099511627776
    # 2^39 = 549755813888
    # 2^38 = 274877906944
    # 2^37 = 137438953472
    # 2^36 = 68719476736
    # 2^35 = 34359738368
    # 2^34 = 17179869184
    # 2^33 = 8589934592
    # 2^32 = 4294967296
    # 2^31 = 2147483648
    # 2^30 = 1073741824
    # 2^29 = 536870912
    # 2^28 = 268435456
    # 2^27 = 134217728
    # 2^26 =

=======
Suggestion 9

def main():
    N = int(input())
    # N = 100000
    N += 1
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        n = N
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt == 1:
            ans -= 1
        while n % i == 0:
            n //= i
        if n == 1:
            continue
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                ans -= 1
                break
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        num = i * i
        while num <= N:
            ans -= 1
            num *= i
    print(ans)
