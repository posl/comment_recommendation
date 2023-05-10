Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    ans = len(s)
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            ans = min(ans, i)
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
main()

=======
Suggestion 6

def solve():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    t = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    S = input()
    T = input()
    ans = len(S)
    for i in range(len(S)):
        count = 0
        for j in range(len(S)):
            if i+j >= len(S):
                if S[i+j-len(S)] != T[j]:
                    count += 1
            else:
                if S[i+j] != T[j]:
                    count += 1
        ans = min(ans, count)
    print(ans)
