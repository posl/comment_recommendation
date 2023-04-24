Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print('Yes')
            return
        s = s[1:] + s[0]
    print('No')
    return

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            return
    print("No")
    return

main()

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, len(S)):
        if S == T[i:] + T[:i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(1, 26):
        if s == ''.join([chr((ord(c) - ord('a') + i) % 26 + ord('a')) for c in t]):
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 7

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            if ord(S[i]) - ord(T[i]) != -25:
                print("No")
                return
    print("Yes")

=======
Suggestion 8

def main():
    S = list(input())
    T = list(input())
    for i in range(len(S)):
        if S[i] != T[i]:
            if ord(S[i]) + (len(S) - i) != ord(T[i]):
                print("No")
                return
    print("Yes")

=======
Suggestion 9

def shiftByK(s, k):
    return ''.join([chr((ord(c) - ord('a') + k) % 26 + ord('a')) for c in s])

=======
Suggestion 10

def is_equal(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True
