Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break

=======
Suggestion 3

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            exit()

=======
Suggestion 4

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            return
    print(len(s)+1)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return
    print(len(S)+1)
    return

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            return
    print(len(t))
    return
