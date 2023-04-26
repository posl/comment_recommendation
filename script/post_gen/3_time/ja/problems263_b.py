Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == n:
            ans += 1
        else:
            ans += 0
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    for i in range(n):
        p[i] -= 1
    ans = 0
    for i in range(n):
        c = 0
        j = i
        while j != -1:
            j = p[j]
            c += 1
        ans = max(ans, c)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += 1
        if p[i] == n:
            break
        else:
            n = p[i]
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 1
    for i in range(1, N):
        if P[i] == N:
            ans += 1
            N = i + 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += 1
        if p[i] > p[i+1]:
            ans = 0
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        ans = max(ans, dfs(p, i))
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    ans = 0
    for i in range(1,n):
        if p[i-1] == n:
            ans = i
            break
        else:
            continue
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = 1
        j = p[i]
        while j > 0:
            ans[i] += 1
            j = p[j - 1]
    print(max(ans))

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans = max(ans, cnt(p, i + 1))

    print(ans)

=======
Suggestion 10

def get_input_data():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p
