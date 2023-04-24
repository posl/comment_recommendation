Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if (ord(t[i]) - ord(s[i]) + 26) % 26 != 0:
            print("No")
            exit()
    print("Yes")
    return

main()

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        elif s[i] == 'a' and t[i] == 'z':
            continue
        elif s[i] == 'z' and t[i] == 'a':
            continue
        elif ord(s[i]) + 1 == ord(t[i]):
            continue
        elif ord(s[i]) - 1 == ord(t[i]):
            continue
        else:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(26):
        if S == T:
            print("Yes")
            return
        S = "".join([chr((ord(s) - ord("a") + 1) % 26 + ord("a")) for s in S])
    print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(1, 26):
        tmp = ''
        for c in s:
            tmp += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
        if tmp == t:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if ord(s[i]) > ord(t[i]):
            if ord(s[i]) - ord(t[i]) <= 13:
                continue
            else:
                print("No")
                return
        else:
            if ord(t[i]) - ord(s[i]) <= 13:
                continue
            else:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 7

def main():
    s = input()
    t = input()

    if s == t:
        print("Yes")
        return

    for i in range(1, 26):
        if "".join([chr((ord(c) - ord("a") + i) % 26 + ord("a")) for c in s]) == t:
            print("Yes")
            return

    print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for k in range(1, 26):
            if s == ''.join([chr((ord(c) - ord('a') + k) % 26 + ord('a')) for c in t]):
                print('Yes')
                return
        print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(1, 26):
        if t == "".join([chr(((ord(c) - 97 + i) % 26) + 97) for c in s]):
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(26):
            if S == T:
                print('Yes')
                exit()
            S = S[1:] + S[0]
    print('No')
