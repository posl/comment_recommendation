Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = ''
    for i in range(len(s)):
        ans += chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in s:
        ans += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    for s in S:
        print(chr(ord('A') + (ord(s) - ord('A') + N) % 26), end='')

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    for s in S:
        print(chr((ord(s) - ord('A') + N) % 26 + ord('A')), end='')
    print()

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    for i in s:
        if ord(i) + n > ord('Z'):
            print(chr(ord(i) + n - ord('Z') + ord('A') - 1), end='')
        else:
            print(chr(ord(i) + n), end='')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        if ord(S[i]) + N > ord("Z"):
            ans += chr(ord(S[i]) + N - ord("Z") + ord("A") - 1)
        else:
            ans += chr(ord(S[i]) + N)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    for i in range(len(S)):
        print(chr(ord("A")+(ord(S[i])-ord("A")+N)%26),end="")
    print()

=======
Suggestion 8

def main():
    n = int(input())
    s = input()

    # ord('A') = 65, ord('Z') = 90
    # chr(65) = 'A', chr(90) = 'Z'
    # ord('A') - ord('A') = 0
    # ord('Z') - ord('A') = 25
    # ord('A') + 1 = 66
    # chr(66) = 'B'

    for c in s:
        # ord(c) + n が ord('Z') より大きいときは、ord('A') + (ord(c) + n - ord('Z') - 1) とする。
        print(chr(ord('A') + (ord(c) + n - ord('A')) % 26), end='')

    print('')

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    # ord('A') = 65
    # ord('Z') = 90
    # ord('A') + 26 = 91
    # ord('Z') + 26 = 116
    # ord('A') + 26 * 2 = 117
    # ord('Z') + 26 * 2 = 142
    # ord('A') + 26 * 3 = 143
    # ord('Z') + 26 * 3 = 168
    # ord('A') + 26 * 4 = 169
    # ord('Z') + 26 * 4 = 194
    # ord('A') + 26 * 5 = 195
    # ord('Z') + 26 * 5 = 220
    # ord('A') + 26 * 6 = 221
    # ord('Z') + 26 * 6 = 246
    # ord('A') + 26 * 7 = 247
    # ord('Z') + 26 * 7 = 272
    # ord('A') + 26 * 8 = 273
    # ord('Z') + 26 * 8 = 298
    # ord('A') + 26 * 9 = 299
    # ord('Z') + 26 * 9 = 324
    # ord('A') + 26 * 10 = 325
    # ord('Z') + 26 * 10 = 350
    # ord('A') + 26 * 11 = 351
    # ord('Z') + 26 * 11 = 376
    # ord('A') + 26 * 12 = 377
    # ord('Z') + 26 * 12 = 402
    # ord('A') + 26 * 13 = 403
    # ord('Z') + 26 * 13 = 428
    # ord('A') + 26 * 14 = 429
    # ord('Z') + 26 * 14 = 454
    # ord('A') + 26 * 15 = 455
    # ord('Z') + 26
