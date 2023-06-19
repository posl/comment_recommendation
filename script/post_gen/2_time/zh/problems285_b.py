Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n and s[l] != s[i + l]:
            l += 1
        print(l)

=======
Suggestion 2

def max_l(s, i):
    l = 0
    while i + l < len(s):
        if s[l] != s[i + l]:
            l += 1
        else:
            break
    return l

=======
Suggestion 3

def solve():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        while i+l < N:
            if S[l] != S[i+l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 4

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
Suggestion 5

def main():
    # 读取输入
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    for i in range(1, N):
        l = 0
        while (i + l < N):
            if (S[l] != S[i + l]):
                l += 1
            else:
                break
        print(l)
    return

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
    for i in range(1, N):
        l = 0
        for k in range(i, N):
            if S[k] != S[k-i]:
                l = k
        print(l)

=======
Suggestion 8

def main():
    n=int(input())
    s=input()
    for i in range(1,n):
        l=0
        while i+l<n and s[l]!=s[i+l]:
            l+=1
        print(l)
main()

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        while l+i < N:
            if S[l] != S[l+i]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 10

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
