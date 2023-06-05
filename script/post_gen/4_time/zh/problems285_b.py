Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        while l+i<N and S[l]!=S[l+i]:
            l+=1
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

def solve():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while l + i < n and s[l] != s[l + i]:
            l += 1
        print(l)

=======
Suggestion 4

def check(s, i):
    n = len(s)
    l = 0
    while i + l < n:
        if s[l] == s[i + l]:
            break
        l += 1
    return l

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 6

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
Suggestion 7

def solve():
    n = int(input())
    s = input()
    for i in range(1, n):
        for j in range(n-i):
            if s[j] == s[j+i]:
                print(i)
                break
        else:
            print(n-i)
solve()

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i+l<n and s[l]!=s[i+l]:
            l+=1
        print(l)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        cnt = 0
        while i+cnt < n:
            if s[cnt] == s[i+cnt]:
                break
            cnt += 1
        print(cnt)

=======
Suggestion 10

def solve():
    n = int(input())
    s = input()
    ans = []
    for i in range(1,n):
        l = 0
        while i+l < n and s[l] != s[i+l]:
            l += 1
        ans.append(l)
    print('\n'.join(map(str,ans)))
