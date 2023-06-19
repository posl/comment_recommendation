Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(0,len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    i = 0
    while i < s_len:
        if s[i] != t[i]:
            break
        i += 1
    print(i+1)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break

=======
Suggestion 6

def main():
    S = input()
    T = input()
    # print(S)
    # print(T)
    for i in range(len(S)):
        if S[0:i] + S[i+1:] == T:
            print(i+1)
            break
    else:
        print(len(S)+1)

=======
Suggestion 7

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    if i == len(s)-1:
        print(len(s)+1)

=======
Suggestion 8

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            exit()

    print(len(s)+1)
