Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = 10**9+1
    for i in range(N):
        if P[i] < min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = p[0]
    count = 1
    for i in range(1, n):
        if p[i] < min:
            min = p[i]
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = p[0]
    for i in range(n):
        if p[i] <= min:
            ans += 1
            min = p[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = n+1
    for i in range(n):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(p)
    ans = 0
    min = n + 1
    for i in range(n):
        if p[i] <= min:
            ans += 1
            min = p[i]
    print(ans)

=======
Suggestion 7

def find_num(s):
    s = s.split()
    n = int(s[0])
    s = s[1:]
    count = 1
    for i in range(1, n):
        if int(s[i]) < int(s[i - 1]):
            count += 1
    return count

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min_p = p[0]
    for i in range(n):
        if min_p >= p[i]:
            ans += 1
            min_p = p[i]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = n + 1
    for i in range(n):
        if p[i] < min:
            min = p[i]
            count += 1
    print(count)

=======
Suggestion 10

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    s = [0] * n
    s[0] = p[0]
    for i in range(1, n):
        s[i] = min(s[i - 1], p[i])
    cnt = 0
    for i in range(n):
        if p[i] <= s[i]:
            cnt += 1
    print(cnt)

solve()
