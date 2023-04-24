Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

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
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    T = input()
    ans = 0
    for s, t in zip(S, T):
        if s != t:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    print(sum([1 for i in range(len(S)) if S[i] != T[i]]))

=======
Suggestion 8

def count_diff_chars(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict

    def input(): return sys.stdin.readline().rstrip()

    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1
    print(cnt)
