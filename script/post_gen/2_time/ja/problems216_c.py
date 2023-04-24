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
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N % 2 == 0:
            S += "B"
            N = N // 2
        else:
            S += "A"
            N -= 1
    print(S[::-1])

=======
Suggestion 5

def main():
    N = int(input())
    S = ""
    while N != 0:
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
            N = N // 2
            S = "B" + S
        else:
            N -= 1
            S = "A" + S
    print(S)

=======
Suggestion 7

def main():
    N = int(input())
    S = ""
    while N > 0:
        if N%2 == 0:
            S = "B" + S
            N //= 2
        else:
            S = "A" + S
            N -= 1
    print(S)

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    while N > 0:
        if N % 2 == 0:
            N = N // 2
            S.append('B')
        else:
            N -= 1
            S.append('A')
    S.reverse()
    print(''.join(S))

=======
Suggestion 9

def main():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            ans = 'B' + ans
            N = N // 2
        else:
            ans = 'A' + ans
            N = N - 1
    print(ans)
