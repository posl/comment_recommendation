Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)
main()

=======
Suggestion 5

def solve():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    t = input()
    n = len(s)
    ans = n
    for i in range(n):
        if s[i:] + s[:i] == t:
            ans = min(ans, i)
    print(ans)
main()

=======
Suggestion 8

def main():
    s = input()
    t = input()

    if s == t:
        print(0)
        exit()
    if len(s) != len(t):
        print(-1)
        exit()
    if len(s) == 1:
        print(1)
        exit()

    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    if ans == 2:
        print(2)
    else:
        print(-1)
main()
