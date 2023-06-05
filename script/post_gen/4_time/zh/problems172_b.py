Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()

    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    print(count)

=======
Suggestion 2

def solve(s,t):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += 1
    return ans

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
        if(s[i] != t[i]):
            count += 1
    print(count)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 6

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
Suggestion 7

def solve():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)
