Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S += "B"
            N //= 2
        else:
            S += "A"
            N -= 1
    print(S[::-1])

=======
Suggestion 2

def main():
    n = int(input())
    s = ''
    while n > 0:
        if n % 2 == 0:
            s += 'B'
            n //= 2
        else:
            s += 'A'
            n -= 1
    print(s[::-1])

=======
Suggestion 3

def main():
    N = int(input())
    ans = ""
    while N > 0:
        if N % 2 == 0:
            ans += "B"
            N //= 2
        else:
            ans += "A"
            N -= 1
    print(ans[::-1])

=======
Suggestion 4

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 1:
            S = "A" + S
            N -= 1
        else:
            S = "B" + S
            N //= 2
    print(S)

main()

=======
Suggestion 5

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            N //= 2
            S += "B"
        else:
            N -= 1
            S += "A"
    print(S[::-1])

=======
Suggestion 6

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            N //= 2
            S = "B" + S
        else:
            N -= 1
            S = "A" + S
    print(S)

=======
Suggestion 7

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            s += "B"
            n /= 2
        else:
            s += "A"
            n -= 1
    print(s[::-1])

=======
Suggestion 8

def main():
    N = int(input())
    result = ""
    while N > 0:
        if N % 2 == 0:
            result += "B"
            N //= 2
        else:
            result += "A"
            N -= 1
    print(result[::-1])

=======
Suggestion 9

def main():
    # Input
    N = int(input())
    # Initialize
    S = ''
    # Process
    while N > 0:
        if N % 2 == 0:
            S = 'B' + S
            N //= 2
        else:
            S = 'A' + S
            N -= 1
    # Output
    print(S)
