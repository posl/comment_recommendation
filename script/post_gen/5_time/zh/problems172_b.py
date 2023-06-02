Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    count = 0
    for i in range(0,len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 3

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
Suggestion 4

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
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
    s = input()
    t = input()
    n = len(s)
    ans = n
    for i in range(n):
        for j in range(n):
            if i + j >= n:
                break
            if s[i + j] != t[j]:
                break
            if i + j == n - 1:
                ans = min(ans, i)
    print(ans)

solve()
