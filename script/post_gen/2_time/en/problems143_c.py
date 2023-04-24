Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    count = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    cnt = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    result = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            result += 1
    print(result)
main()

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)

    cnt = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            cnt += 1

    print(cnt)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    print(solve(N, S))
