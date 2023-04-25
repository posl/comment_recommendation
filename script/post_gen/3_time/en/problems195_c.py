Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N < 1000:
        print(0)
    elif N < 1000000:
        print(N-999)
    elif N < 1000000000:
        print(999000 + (N-999999)*2)
    elif N < 1000000000000:
        print(999000000 + (N-999999999)*3)
    else:
        print(999000000000 + (N-999999999999)*4)
main()

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    if N < 1000:
        ans = 0
    elif N < 1000000:
        ans = N - 999
    elif N < 1000000000:
        ans = 1000000 - 1000 + (N - 999999) * 2
    elif N < 1000000000000:
        ans = 1000000000 - 1000000 + 1999000 + (N - 999999999) * 3
    elif N < 1000000000000000:
        ans = 1000000000000 - 1000000000 + 2999000000 + (N - 999999999999) * 4
    else:
        ans = 1000000000000000 - 1000000000000 + 3999000000000 + (N - 999999999999999) * 5
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    print(N - N//(10**3) - N//(10**6) - N//(10**9) - N//(10**12) - N//(10**15))

main()

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * (10 ** i - 10 ** (i - 1))
    ans += (len(str(N)) - 1) * (N - 10 ** (len(str(N)) - 1) + 1)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * (10 ** i - 10 ** (i - 1))
    ans += (len(str(N)) * (N - 10 ** (len(str(N)) - 1) + 1))
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, len(str(n))):
        ans += i * (10 ** i - 10 ** (i - 1))
    ans += len(str(n)) * (n - 10 ** (len(str(n)) - 1) + 1)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    i = 1
    while i <= N:
        ans += (N - i + 1) * (len(str(i)) - 1)
        i *= 1000
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1, 16):
        if N >= 10 ** (3 * i):
            ans += 3 * 10 ** (3 * (i - 1))
        else:
            ans += (N - 10 ** (3 * (i - 1)) + 1) * i
            break
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(0, len(str(N))):
        if N // (10 ** (3 * i)) == 0:
            break
        ans += (N // (10 ** (3 * i))) - 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    print((N+3)//3-1)
