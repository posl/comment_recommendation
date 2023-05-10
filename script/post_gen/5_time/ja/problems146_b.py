Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        ans += chr(65 + (ord(s[i]) - 65 + n) % 26)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    ans = ''
    for i in range(len(S)):
        if ord(S[i]) + N > 90:
            ans += chr(ord(S[i]) + N - 26)
        else:
            ans += chr(ord(S[i]) + N)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        ans += chr((ord(S[i]) - ord('A') + N) % 26 + ord('A'))
    print(ans)

=======
Suggestion 4

def main():
    # N = input()
    # S = input()
    N = 13
    S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # N = 2
    # S = "ABCXYZ"
    N = int(N)
    S = list(S)
    # print(S)
    # print(ord('A'))
    # print(ord('Z'))
    # print(ord('a'))
    # print(ord('z'))
    for i in range(len(S)):
        # print(S[i])
        # print(ord(S[i]))
        # print(ord(S[i]) + N)
        # print(ord(S[i]) + N - ord('Z'))
        # print(ord(S[i]) + N - ord('Z') + ord('A'))
        if ord(S[i]) + N <= ord('Z'):
            # print(chr(ord(S[i]) + N))
            S[i] = chr(ord(S[i]) + N)
        else:
            # print(chr(ord(S[i]) + N - ord('Z') + ord('A') - 1))
            S[i] = chr(ord(S[i]) + N - ord('Z') + ord('A') - 1)
    print("".join(S))

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    for i in range(len(S)):
        if ord(S[i]) + N > 90:
            print(chr(ord(S[i]) + N - 26), end='')
        else:
            print(chr(ord(S[i]) + N), end='')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    ans = ''
    for s in S:
        ans += chr((ord(s)-ord('A')+N)%26+ord('A'))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        ans += chr(((ord(S[i]) - ord('A') + N) % 26) + ord('A'))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    ans = ''
    for i in s:
        ans += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    ans = ''
    for i in range(len(s)):
        ans += chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    ans = []
    for i in s:
        ans.append(chr((ord(i) - ord('A') + n) % 26 + ord('A')))
    print(''.join(ans))
