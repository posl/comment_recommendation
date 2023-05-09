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
    S = input()
    T = input()
    for i in range(len(S)):
        if S[:i] + S[i+1:] == T:
            print(i+1)
            break

=======
Suggestion 5

def main():
    s = list(input())
    t = list(input())
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

=======
Suggestion 6

def main():
    S = input()
    T = input()
    for i in range(len(T)):
        if T[i] != S[i]:
            print(i+1)
            break
