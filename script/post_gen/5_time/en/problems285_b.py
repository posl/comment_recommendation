Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] != S[i + l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        for j in range(n - i):
            if s[j] != s[j + i]:
                l = j + 1
        print(l)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while l+i < N:
            if S[l] != S[l+i]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        while i + l < N:
            if S[l] == S[i+l]:
                break
            l += 1
        print(l)

=======
Suggestion 6

def problems285_b():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] == s[l + i]:
                break
            l += 1
        print(l)

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    L = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            if S[i] != S[j]:
                L[i] = max(L[i], j-i)
            else:
                break
    for i in range(N-1):
        print(L[i])

=======
Suggestion 9

def max_non_repeat_len(s):
    """Return the maximum non-negative integer l that satisfies all of the following conditions:
    l+i ≦ N, and
    for all integers k such that 1 ≦ k ≦ l, it holds that S_{k} ≠ S_{k+i}.
    Note that l=0 always satisfies the conditions.
    """
    n = len(s)
    max_l = 0
    for i in range(1, n):
        l = 0
        while (l+i < n) and (s[l] != s[l+i]):
            l += 1
        if l > max_l:
            max_l = l
    return max_l
