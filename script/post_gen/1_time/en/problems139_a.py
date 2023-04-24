Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(3):
        if s[i] == t[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    c = 0
    for i in range(3):
        if S[i] == T[i]:
            c += 1
    print(c)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    print(sum([1 for i in range(3) if S[i] == T[i]]))

=======
Suggestion 5

def main():
    s = input()
    t = input()
    print(sum(s[i] == t[i] for i in range(3)))

=======
Suggestion 6

def read_line():
    return input()
