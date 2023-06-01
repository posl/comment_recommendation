Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while l + i < N:
            if S[l] != S[l + i]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i+l < n:
            if s[l] != s[i+l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 3

def problem285_b():
    pass

=======
Suggestion 4

def solve():
    N = int(input())
    S = input()
    ans = [0] * (N - 1)
    for i in range(1, N):
        for j in range(N - i):
            if S[j] != S[i + j]:
                ans[i - 1] = i
                break
    print(*ans, sep='\n')

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] == S[i + l]:
                break
            l += 1
        print(l)

=======
Suggestion 6

def get_max_l(s, i):
    l = 0
    while (i + l < len(s)):
        if (s[l] != s[i + l]):
            l = l + 1
        else:
            break
    return l

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        ans = 0
        while i + ans < n and s[ans] != s[i + ans]:
            ans += 1
        print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i + l < n and s[l] != s[i+l]:
            l += 1
        print(l)
