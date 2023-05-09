Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = N - 1
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    if N == 2:
        print(1)
        return
    if N == 3:
        print(2)
        return
    if N == 4:
        print(2)
        return
    if N == 5:
        print(3)
        return
    if N == 6:
        print(3)
        return
    if N == 7:
        print(4)
        return
    if N == 8:
        print(4)
        return
    if N == 9:
        print(3)
        return
    if N == 10:
        print(4)
        return
    if N == 11:
        print(5)
        return
    if N == 12:
        print(4)
        return
    if N == 13:
        print(5)
        return
    if N == 14:
        print(5)
        return
    if N == 15:
        print(6)
        return
    if N == 16:
        print(5)
        return
    if N == 17:
        print(6)
        return
    if N == 18:
        print(6)
        return
    if N == 19:
        print(7)
        return
    if N == 20:
        print(6)
        return
    if N == 21:
        print(7)
        return
    if N == 22:
        print(7)
        return
    if N == 23:
        print(8)
        return
    if N == 24:
        print(7)
        return
    if N == 25:
        print(8)
        return
    if N == 26:
        print(8)
        return
    if N == 27:
        print(9)
        return
    if N == 28:
        print(8)
        return
    if N == 29:
        print(9)
        return
    if N == 30:
        print(9)
        return
    if N == 31:
        print(10)
        return
    if N == 32:
        print(9)
        return
    if N == 33:
        print(10)
        return
    if N == 34:
        print(10)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N -= 1
            ans += 1
    print(ans + 1)

=======
Suggestion 4

def main():
    N = int(input())
    i = 1
    j = 1
    count = 0
    while i*j < N:
        if i < j:
            i += 1
        else:
            j += 1
        count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    result = 0
    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            result += 1
    print(result)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n = n-1
            ans = ans+1
    ans = ans+1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    while N>1:
        if N%2 == 0:
            N = N//2
        else:
            N = N-1
            ans += 1
    print(ans+1)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans = max(ans, i - 1 + n // i - 1)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    while(N != 0):
        if N % 2 == 0:
            N /= 2
            ans += 1
        else:
            N -= 1
            ans += 1
    print(ans)
