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
            ans = 0
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == n:
            ans += 1
        else:
            ans = 1
            j = i
            while p[j] != n:
                j = p[j] - 1
                ans += 1
            break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if p[i] == n:
            break
        else:
            n = p[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    p = [int(x) - 1 for x in input().split()]
    ans = 0
    for i in range(n):
        now = i
        cnt = 0
        while now != -1:
            now = p[now]
            cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans = max(ans, p[i] + 1)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if (i+1) == P[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans = max(ans, f(i, p))
    print(ans)

=======
Suggestion 8

def parent(n, p):
    if p[n-1] == 1:
        return 1
    else:
        return 1 + parent(p[n-1], p)

=======
Suggestion 9

def count_parent(n,p):
    if p == 1:
        return 1
    else:
        return count_parent(n,p-1) + 1

n = int(input())
p = list(map(int,input().split()))

print(count_parent(n,p[-1]))

=======
Suggestion 10

def calc_generation(n, parents, child):
    if n == 1:
        return 0
    else:
        return calc_generation(n-1, parents, child) + 1
