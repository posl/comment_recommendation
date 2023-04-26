Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    S = input()
    T = input()
    flag = False
    for i in range(len(S)):
        if S[i] == T[i]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if t[i] == s[i]:
            continue
        if t[i] == "a" and s[i] == "z":
            continue
        if t[i] == "z" and s[i] == "a":
            continue
        if t[i] == "b" and s[i] == "y":
            continue
        if t[i] == "y" and s[i] == "b":
            continue
        if t[i] == "c" and s[i] == "x":
            continue
        if t[i] == "x" and s[i] == "c":
            continue
        if ord(t[i]) - ord(s[i]) == 1:
            continue
        if ord(s[i]) - ord(t[i]) == 1:
            continue
        print("No")
        return
    print("Yes")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        S = S[1:] + S[0]
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for k in range(26):
        for i in range(len(s)):
            if ord(t[i]) - ord(s[i]) != k and ord(t[i]) - ord(s[i]) != k - 26:
                break
        else:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for k in range(1, 26):
        if s == t[k:] + t[:k]:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        if "".join([chr((ord(c) - ord("a") + i) % 26 + ord("a")) for c in S]) == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    S = input()
    T = input()

    if S == T:
        print("Yes")
        return

    for i in range(1, 26):
        S = "".join([chr((ord(c) - ord("a") + i) % 26 + ord("a")) for c in S])
        if S == T:
            print("Yes")
            return

    print("No")

=======
Suggestion 10

def get_input():
    S = input()
    T = input()
    return S, T
