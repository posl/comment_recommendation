Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    ans = [0 for _ in range(n-1)]
    for i in range(n-1):
        l = 0
        while i+l < n-1 and s[l] != s[i+l]:
            l += 1
        ans[i] = l
    print(*ans, sep='\n')

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] == S[i + l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    #print(n, s)
    for i in range(1, n):
        #print(i)
        count = 0
        for j in range(0, n-i):
            #print(j)
            if s[j] != s[j+i]:
                count += 1
        print(count)
    return

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                l += 1
            else:
                break
        count = max(count, l)
        print(count)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    ans = []
    for i in range(1,n):
        l = 0
        while i + l < n:
            if s[l] != s[i+l]:
                l += 1
            else:
                break
        ans.append(l)
    for a in ans:
        print(a)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    # print(N)
    # print(S)
    for i in range(1, N):
        # print(i)
        for l in range(1, N-i+1):
            # print(l)
            if S[l-1] == S[l-1+i]:
                break
        print(l-1)

=======
Suggestion 7

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
main()

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        for j in range(N-i):
            if S[j] != S[i+j]:
                l = j+1
        print(l)

=======
Suggestion 9

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
Suggestion 10

def count(s, i):
    l = 0
    while i + l < len(s):
        if s[l] != s[i + l]:
            l += 1
        else:
            break
    return l

n = int(input())
s = input()
for i in range(1, n):
    print(count(s, i))
