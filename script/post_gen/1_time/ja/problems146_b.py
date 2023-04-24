Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            ans += chr(ord(s[i]) + n - 26)
        else:
            ans += chr(ord(s[i]) + n)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        ans += chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        ans += chr((ord(s[i]) - 65 + n) % 26 + 65)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        if ord(S[i]) + N > 90:
            ans += chr(ord(S[i]) + N - 26)
        else:
            ans += chr(ord(S[i]) + N)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    ans = ''
    for i in range(len(s)):
        if ord(s[i]) + n > ord('Z'):
            ans += chr(ord(s[i]) + n - ord('Z') + ord('A') - 1)
        else:
            ans += chr(ord(s[i]) + n)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = ''
    for i in range(len(s)):
        ans += chr(((ord(s[i]) - ord('A') + n) % 26) + ord('A'))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()

    ans = ""
    for s in S:
        ans += chr((ord(s) - ord("A") + N) % 26 + ord("A"))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = list(input())
    ans = []
    for i in range(len(s)):
        ans.append(chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')))
    print(''.join(ans))

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in range(len(s)):
        for j in range(len(alpha)):
            if s[i] == alpha[j]:
                ans += alpha[(j+n)%26]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    result = ""
    for s in S:
        ascii_num = ord(s)
        ascii_num += N
        if ascii_num > 90:
            ascii_num -= 26
        result += chr(ascii_num)
    print(result)
