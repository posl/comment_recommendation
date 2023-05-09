Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = ''
    while n > 0:
        if n % 2 == 1:
            s = 'A' + s
            n -= 1
        else:
            s = 'B' + s
            n //= 2
    print(s)

=======
Suggestion 2

def main():
    N = int(input())
    S = ''
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            S = 'B' + S
        else:
            N = N - 1
            S = 'A' + S
    print(S)

=======
Suggestion 3

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            s = "B" + s
        else:
            n -= 1
            s = "A" + s
    print(s)

=======
Suggestion 4

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            s += "B"
            n //= 2
        else:
            s += "A"
            n -= 1
    print(s[::-1])

=======
Suggestion 5

def main():
    n = int(input())
    ans = ''
    while n > 0:
        if n % 2 == 1:
            ans = 'A' + ans
            n -= 1
        else:
            ans = 'B' + ans
            n //= 2
    print(ans)
    return None

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    while n > 0:
        if n % 2 == 0:
            s.append('B')
            n = n // 2
        else:
            s.append('A')
            n -= 1
    print(''.join(s[::-1]))

=======
Suggestion 7

def main():
    n = int(input())
    ans = ""
    while n > 0:
        if n % 2 == 0:
            ans = "B" + ans
            n = n // 2
        else:
            ans = "A" + ans
            n -= 1
    print(ans)

=======
Suggestion 8

def solve(N):
    if N == 1:
        return "A"
    elif N == 2:
        return "AA"
    elif N == 3:
        return "AAA"
    elif N == 4:
        return "AAB"
    elif N == 5:
        return "AABA"
    elif N == 6:
        return "AAAB"
    elif N == 7:
        return "AAABA"
    elif N == 8:
        return "AAABB"
    elif N == 9:
        return "AAABAB"
    elif N == 10:
        return "AAABBB"
    elif N == 11:
        return "AAABABA"
    elif N == 12:
        return "AAABABB"
    elif N == 13:
        return "AAABABBA"
    elif N == 14:
        return "AAABABBB"
    elif N == 15:
        return "AAABABABA"
    elif N == 16:
        return "AAABABABB"
    elif N == 17:
        return "AAABABABBA"
    elif N == 18:
        return "AAABABABBB"
    elif N == 19:
        return "AAABABABABA"
    elif N == 20:
        return "AAABABABABB"
    elif N == 21:
        return "AAABABABABBA"
    elif N == 22:
        return "AAABABABABBB"
    elif N == 23:
        return "AAABABABABABA"
    elif N == 24:
        return "AAABABABABABB"
    elif N == 25:
        return "AAABABABABABBA"
    elif N == 26:
        return "AAABABABABABBB"
    elif N == 27:
        return "AAABABABABABABA"
    elif N == 28:
        return "AAABABABABABABB"
    elif N == 29:
        return "AAABABABABABABBA"
    elif N == 30:
        return "AAABABABABABABBB"
    elif N == 31:
        return "AAABABABABABABABA"
    elif N == 32:
        return "AAABABABABABABABB"

=======
Suggestion 9

def main():
    # N = int(input())
    N = 5

    # 2^0 + 2^2 + 2^4 + ... + 2^x <= N
    # 2^0 + 2^1 + 2^2 + 2^3 + ... + 2^x <= N
    # 2^(x+1) - 1 <= N
    # x = log2(N+1) - 1
    x = int(math.log2(N+1) - 1)
    print(x)

    # 2^0 + 2^2 + 2^4 + ... + 2^x = N
    # 2^0 + 2^1 + 2^2 + 2^3 + ... + 2^x = N
    # 2^(x+1) - 1 = N
    # x = log2(N+1) - 1

    # 2^0 + 2^1 + 2^2 + 2^3 + ... + 2^x + 2^(x+1) - 1 = N
    # 2^(x+2) - 1 = N
    # x = log2(N+1) - 2

    # 2^0 + 2^1 + 2^2 + 2^3 + ... + 2^x + 2^(x+1) + 2^(x+2) - 1 = N
    # 2^(x+3) - 1 = N
    # x = log2(N+1) - 3

    # 2^0 + 2^1 + 2^2 + 2^3 + ... + 2^x + 2^(x+1) + 2^(x+2) + 2^(x+3) - 1 = N
    # 2^(x+4) - 1 = N
    # x = log2(N+1) - 4

    # 2^0 + 2^1 + 2^2 + 2^3 + ... + 2^x + 2^(x+1) + 2^(x+2) + 2^(x+3) + 2^(x
