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
    return

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        while i+l < n and s[l] != s[i+l]:
            l += 1
        print(l)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    for i in range(1,n):
        l = 0
        for j in range(n-i):
            if s[j] != s[i+j]:
                l = j+1
        print(l)
    return

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for k in range(i,N):
            if S[k] != S[k-i]:
                l = k
        print(l)
    return 0

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = [0] * (n-1)
    for i in range(1, n):
        for j in range(n-i):
            if s[j] != s[j+i]:
                ans[i-1] = i
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    for i in range(n):
        cnt = 0
        for j in range(n - i - 1):
            if s[j] != s[j + i + 1]:
                cnt += 1
            else:
                cnt = 0
            if j == n - i - 2:
                print(cnt)
main()

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] != S[i + l]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 9

def count_non_repeat(string, i):
    count = 0
    for j in range(i, len(string)):
        if string[j] != string[j+i]:
            count += 1
        else:
            break
    return count

=======
Suggestion 10

def main():
    # Get input here
    N = int(input())
    S = input()

    # Solve problems
    # for i in range(1, N):
    #     print(i)
    #     l = 0
    #     for k in range(1, N - i + 1):
    #         if S[k - 1] != S[k - 1 + i]:
    #             l += 1
    #         else:
    #             break
    #     print(l)
    #     print()
    #     # print(i)
    #     # print(l)
