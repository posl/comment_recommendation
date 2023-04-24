Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    i = 1
    while i <= n:
        ans += (n - i + 1)
        i *= 1000
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * 3 * (10 ** (i - 1))
    ans += (N - 10 ** (len(str(N)) - 1) + 1) * len(str(N))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    N = N + 1
    N = str(N)
    N = N[::-1]
    ans = 0
    for i in range(len(N)):
        if i % 3 == 2:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    print((len(str(N)) - 1) // 3)

=======
Suggestion 5

def main():
    N = int(input())
    Nstr = str(N)
    Nlen = len(Nstr)
    if Nlen < 4:
        print(0)
    else:
        Nlen -= 3
        print(Nlen + Nlen // 2)

=======
Suggestion 6

def main():
    N = input()
    N = N[::-1]
    print(sum([i for i in range(len(N)) if i % 3 == 2]))

=======
Suggestion 7

def main():
    n = int(input())
    print((len(str(n))-1)//3)
