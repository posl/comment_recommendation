Synthesizing 10/10 solutions

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
        ans += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        ans += chr((ord(S[i]) - ord("A") + N) % 26 + ord("A"))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        num = ord(S[i]) + N
        if num > 90:
            num -= 26
        ans += chr(num)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    result = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            result += chr(ord(s[i]) + n - 26)
        else:
            result += chr(ord(s[i]) + n)
    print(result)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        ans += chr((ord(s[i])-ord("A")+n)%26+ord("A"))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = ''
    for s in S:
        ans += chr(((ord(s) - ord('A')) + N) % 26 + ord('A'))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()

    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in range(len(s)):
        ans += alp[(alp.index(s[i]) + n) % 26]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    a = []
    for i in range(len(s)):
        a.append(chr(ord(s[i])+n))
        if ord(a[i]) > 90:
            a[i] = chr(ord(a[i])-26)
    print(''.join(a))

=======
Suggestion 10

def main():
    N = int(input())
    S = input()

    ans = ''
    for s in S:
        ans += chr((ord(s)-65+N)%26+65)
    print(ans)
