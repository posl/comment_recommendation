Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while l + i < n:
            if s[l] != s[l + i]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 2

def problem285_b():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while(i + l < n):
            if(s[l] == s[i+l]):
                break
            l += 1
        print(l)
    return

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    s = input()
    for i in range(n-1):
        l = 0
        while i + l < n and i + l * 2 < n and s[i] != s[i + l] and s[i + l] != s[i + l * 2]:
            l += 1
        print(l)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i + l < n and s[l] != s[i+l]:
            l += 1
        print(l)

=======
Suggestion 6

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
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = []
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] != S[i + l]:
                l += 1
            else:
                break
        ans.append(l)
    print("\n".join(map(str, ans)))

=======
Suggestion 8

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
Suggestion 9

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                break
            l += 1
        print(l)
