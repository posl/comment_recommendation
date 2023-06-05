Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    for i in range(n-1):
        l = 0
        while i + l < n and s[l] != s[i+l]:
            l += 1
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

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n and s[l] != s[i + l]:
            l += 1
        print(l)

=======
Suggestion 4

def get_max_l(S, i):
    N = len(S)
    l = 0
    while l + i < N:
        if S[l] != S[l + i]:
            l += 1
        else:
            break
    return l

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while i + l < N and S[l] != S[i + l]:
            l += 1
        print(l)
main()

=======
Suggestion 6

def solve():
    N = int(input())
    S = input()
    ans = [0] * (N - 1)
    for i in range(1, N):
        for j in range(N - i):
            if S[j] != S[j + i]:
                ans[i - 1] = i
                break
    for i in range(N - 1):
        print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] != S[i+l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 8

def solve():
    N = int(input())
    S = input()
    result = []
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] != S[i + l]:
                l += 1
            else:
                break
        result.append(l)
    for i in result:
        print(i)

=======
Suggestion 9

def solve():
    N = int(input())
    S = input()
    for i in range(1,N):
        count = 0
        for j in range(i,N):
            if S[j-i] != S[j]:
                count += 1
        print(count)
