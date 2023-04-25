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
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    l = len(s)
    ans = 0
    for i in range(l):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    T = input()
    print(sum([1 for i in range(len(S)) if S[i] != T[i]]))

=======
Suggestion 7

def main():
    s = input()
    t = input()
    print(sum(1 for x, y in zip(s, t) if x != y))

=======
Suggestion 8

def solve():
    s = input()
    t = input()
    print(sum([1 for i in range(len(s)) if s[i] != t[i]]))

solve()
