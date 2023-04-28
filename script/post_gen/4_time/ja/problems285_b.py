Synthesizing 10/10 solutions

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

def solve():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n and s[l] != s[i + l]:
            l += 1
        print(l)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        count = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                count += 1
        print(count)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i+l < n and s[l] != s[i+l]:
            l += 1
        print(l)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while True:
            if i + l >= N:
                break
            if S[l] == S[i+l]:
                break
            l += 1
        print(l)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = [0] * (n - 1)
    for i in range(1, n):
        for j in range(n - i):
            if s[j] != s[j + i]:
                ans[i - 1] = i
                break
    for i in range(n - 1):
        print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while (i + l < N) and (S[l] != S[i + l]):
            l += 1
        print(l)

=======
Suggestion 8

def solve():
    N = int(input())
    S = input()
    ans = [0] * (N - 1)
    for i in range(1, N):
        for l in range(N - i):
            if S[l] != S[l + i]:
                ans[i - 1] = i
                break
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    ans = [0 for i in range(n-1)]
    for i in range(1,n):
        for j in range(n-i):
            if s[j] != s[j+i]:
                ans[i-1] += 1
    for i in range(n-1):
        print(ans[i])

=======
Suggestion 10

def main():
    #n = int(input())
    #s = input()
    n = 6
    s = "abcbac"

    for i in range(1, n):
        l = 0
        while True:
            if i + l >= n:
                break
            if s[l] == s[i+l]:
                break
            l += 1
        print(l)
