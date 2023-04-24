Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N < 1000:
        print(0)
    elif N < 1000000:
        print(N - 999)
    elif N < 1000000000:
        print((N - 999999) * 2 + 999)
    elif N < 1000000000000:
        print((N - 999999999) * 3 + 1998)
    elif N < 1000000000000000:
        print((N - 999999999999) * 4 + 2997)
    else:
        print((N - 999999999999999) * 5 + 3996)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * (10 ** i - 10 ** (i - 1))
    ans += len(str(N)) * (N - 10 ** (len(str(N)) - 1) + 1)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * 9 * (10 ** (i - 1))
    ans += len(str(N)) * (N - (10 ** (len(str(N)) - 1)) + 1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += 999 * i * 10 ** (i - 1)
    ans += (N - 10 ** (len(str(N)) - 1) + 1) * len(str(N))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    ans = 0
    for i in range(N_len):
        if i % 3 == 0 and i != 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = str(N)
    L = len(S)
    ans = 0
    for i in range(L):
        if i % 3 == 0 and i != 0:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(3,len(str(N))+1):
        ans += (N-10**(i-1)+1) * (i-1)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    i = 1
    res = 0
    while i <= N:
        res += (N - i + 1) * (len(str(i)) - 1) // 3
        i *= 1000
    print(res)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    i = 1
    while N >= 1000:
        ans += N % 1000
        N //= 1000
        ans += 1
        i += 1
    ans += N
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    print(N - 999 + (N - 1000) // 3 + 1 if N > 1000 else N)
