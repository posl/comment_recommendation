Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        i = str(i)
        if i[0] == i[-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def calc(n):
    ans = 0
    for i in range(1, n+1):
        s = str(i)
        if s[-1] == s[0]:
            ans += 1
    return ans

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        i = str(i)
        if i[0] == i[-1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        s = str(i)
        ans += s.count(s[0]+s[-1])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    if N < 10:
        print(N)
        return
    if N < 100:
        print(9)
        return
    if N < 1000:
        print(9 + (N-99))
        return
    if N < 10000:
        print(9 + 900)
        return
    if N < 100000:
        print(9 + 900 + (N-9999))
        return
    if N < 1000000:
        print(9 + 900 + 90000)
        return
    if N < 10000000:
        print(9 + 900 + 90000 + (N-999999))
        return
    if N < 100000000:
        print(9 + 900 + 90000 + 9000000)
        return
    if N < 1000000000:
        print(9 + 900 + 90000 + 9000000 + (N-99999999))
        return
    if N < 10000000000:
        print(9 + 900 + 90000 + 9000000 + 900000000)
        return
    if N < 100000000000:
        print(9 + 900 + 90000 + 9000000 + 900000000 + (N-9999999999))
        return
    if N < 1000000000000:
        print(9 + 900 + 90000 + 9000000 + 900000000 + 90000000000)
        return
    if N < 10000000000000:
        print(9 + 900 + 90000 + 9000000 + 900000000 + 90000000000 + (N-999999999999))
        return
    if N < 100000000000000:
        print(9 + 900 + 90000 + 9000000 + 900000000 + 90000000000 + 9000000000000)
        return
    if N < 1000000000000000:
        print(9 + 900 + 90000 + 9000000 + 900000000 + 90000000000 + 9000000000000 + (N-99999999999999))
        return

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i % 10 == 0:
            continue
        tmp = i
        while tmp < n+1:
            if tmp % 10 == i // (10 ** len(str(i))-1):
                ans += 1
            tmp *= 10
            tmp += i % 10
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 10 == 0:
            continue
        s = str(i)
        if s[0] == s[-1]:
            ans += 1
    print(ans)
main()

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        i = str(i)
        if i[0] == i[-1]:
            ans += 1
    print(ans)
main()

=======
Suggestion 9

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        s = str(i)
        ans += s.count(s[0]) * s.count(s[-1])
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        s = str(i)
        a = s[0]
        b = s[-1]
        if a == b:
            ans += 1
    print(ans)
