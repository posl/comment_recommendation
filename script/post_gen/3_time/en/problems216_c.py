Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    S = ''
    while N > 0:
        if N % 2 == 0:
            S += 'B'
            N //= 2
        else:
            S += 'A'
            N -= 1
    print(S[::-1])
main()

=======
Suggestion 3

def main():
    n = int(input())
    ans = ""
    while n > 0:
        if n % 2 == 0:
            ans += "B"
            n //= 2
        else:
            ans += "A"
            n -= 1
    print(ans[::-1])

=======
Suggestion 4

def main():
    N = int(input())
    ans = ""
    while N > 0:
        if N % 2 == 1:
            ans += "A"
            N -= 1
        else:
            ans += "B"
            N //= 2
    print(ans[::-1])

=======
Suggestion 5

def main():
    n = int(input())
    s = ""
    while n > 0:
        if n % 2 == 0:
            n //= 2
            s += "B"
        else:
            n -= 1
            s += "A"
    print(s[::-1])

=======
Suggestion 6

def main():
    N = int(input())
    S = ''
    while N > 0:
        if N % 2 == 0:
            N //= 2
            S += 'B'
        else:
            N -= 1
            S += 'A'
    print(S[::-1])

=======
Suggestion 7

def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 1:
            ans += 'A'
            N -= 1
        else:
            ans += 'B'
            N //= 2
    ans = ans[::-1]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = ''
    while n != 0:
        if n % 2 == 0:
            n //= 2
            s += 'B'
        else:
            n -= 1
            s += 'A'
    print(s[::-1])

=======
Suggestion 9

def main():
    N = int(input())
    s = ''
    while N > 0:
        if N % 2 == 1:
            N -= 1
            s += 'A'
        else:
            N //= 2
            s += 'B'
    print(s[::-1])

=======
Suggestion 10

def get_input():
    return int(input())
