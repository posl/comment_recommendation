Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")

solve()

=======
Suggestion 2

def get_str():
    s = input()
    t = input()
    return s, t

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def problem232_b():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(1, 26):
        tmp = ""
        for j in range(len(s)):
            if ord(s[j]) + i > 122:
                tmp += chr(ord(s[j]) + i - 26)
            else:
                tmp += chr(ord(s[j]) + i)
        if tmp == t:
            print("Yes")
            return
    print("No")
    return

problem232_b()

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            diff = ord(T[i]) - ord(S[i])
            if diff < 0:
                diff = diff + 26
            if diff == 1:
                continue
            else:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 6

def func(s,t):
    if not s or not t or len(s) != len(t):
        return False
    if s == t:
        return True
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            if ord(s[i]) > ord(t[i]):
                return False
            else:
                return True
    return False

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            k = ord(t[i]) - ord(s[i])
            if k < 0:
                k += 26
            for j in range(i, len(s)):
                if s[j] != t[j]:
                    if ord(s[j]) - ord('a') != (ord(t[j]) - ord('a') + k) % 26:
                        print("No")
                        return
            print("Yes")
            return
    print("Yes")
    return

=======
Suggestion 8

def move_right(s, n):
    new_s = ''
    for c in s:
        new_s += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    return new_s

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

solve()

=======
Suggestion 10

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print("Yes")
            break
        else:
            s = s[1:] + s[0]
    else:
        print("No")
