Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()

    for i in range(len(S)):
        if S[i] != T[i]:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    t_len = len(t)
    for i in range(t_len):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        for j in range(26):
            if s[i] == chr(ord("a") + j):
                s = s[:i] + chr(ord("a") + (j + 1) % 26) + s[i + 1:]
                break
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def problem232_b():
    s = input()
    t = input()

    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 10

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)

    lenS = len(S)
    #print(lenS)
    lenT = len(T)
    #print(lenT)

    if lenS != lenT:
        print("No")
        exit()

    for i in range(lenS):
        if S[i] != T[i]:
            print("No")
            exit()

    print("Yes")
