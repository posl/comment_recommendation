Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l += 1
        print(l)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(1,N-i+1):
            if S[j-1] != S[j+i-1]:
                l = j
        print(l)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    for i in range(N-1):
        l = 0
        for j in range(N-i-1):
            if S[j] != S[j+i+1]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        for k in range(1, n - i):
            if s[k - 1] != s[k + i - 1]:
                l = k
        print(l)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        for j in range(N-i):
            if S[j] == S[j+i]:
                print(j)
                break
        else:
            print(N-i)

=======
Suggestion 6

def solve():
    N = int(input())
    S = input()
    ans = []
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l += 1
            else:
                break
        ans.append(l)
    print(*ans, sep='

')

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        S1 = S[:i]
        S2 = S[i:]
        l = 0
        for j in range(i):
            if S1[j] != S2[j]:
                l += 1
        print(l)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        S1 = S[i:]
        S2 = S[:N-i]
        l = 0
        for j in range(N-i):
            if S1[j] != S2[j]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        s = S[:i]
        t = S[i:]
        l = 0
        for j in range(1,len(s)+1):
            if s[-j] != t[-j]:
                l = j
                break
        print(l)
