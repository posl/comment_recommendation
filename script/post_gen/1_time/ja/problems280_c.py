Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] == t[:i] and s[i:] == t[i+1:]:
            print(i+1)
            break

=======
Suggestion 2

def main():
    S = input()
    T = input()
    for i in range(len(S)+1):
        if S[:i] == T[:i] and S[i:] == T[i+1:]:
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
            break
    else:
        print(len(S)+1)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)
main()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            exit()
    print(len(s)+1)

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] + s[i-1:] == t:
            print(i)
            break

=======
Suggestion 7

def main():
    s = input()
    t = input()

    for i in range(len(s)+1):
        if s[:i] + s[i-1:] == t:
            print(i)
            exit()

=======
Suggestion 8

def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] + s[i:] == t:
            print(i+1)
            break

=======
Suggestion 9

def main():
    S = input()
    T = input()
    for i in range(len(S)+1):
        if S[:i] + S[i:] == T:
            print(i+1)
            break

=======
Suggestion 10

def main():
    S = input()
    T = input()
    T = list(T)
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            break
    else:
        print(len(S)+1)
