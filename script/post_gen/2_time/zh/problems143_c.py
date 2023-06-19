Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    s = input()
    return n,s

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    count = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            ans += 1
    print(ans)
    return 0

=======
Suggestion 6

def solve():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1,N):
        if S[i-1] != S[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            count += 1
    print(count)

=======
Suggestion 8

def merge_slime(slime):
    if len(slime) == 1:
        return 1
    else:
        return merge_slime(slime[1:]) + 1

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    count = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)
main()
