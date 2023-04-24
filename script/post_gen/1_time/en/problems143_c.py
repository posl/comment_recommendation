Synthesizing 10/10 solutions (Duplicates hidden)

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
    N = int(input())
    S = input()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    slimes = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            slimes += 1
    print(slimes)

=======
Suggestion 5

def solve():
    N = int(input())
    S = input()
    ans = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    print(ans)

solve()

=======
Suggestion 6

def count_slimes(s):
    count = 1
    prev = s[0]
    for c in s[1:]:
        if c != prev:
            count += 1
            prev = c
    return count
