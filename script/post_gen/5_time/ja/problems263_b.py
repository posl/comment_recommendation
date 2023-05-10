Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i + 1 == p[p[i] - 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    for i in range(n):
        cnt = 0
        j = i
        while j > 0:
            j = p[j - 1]
            cnt += 1
        if cnt > max:
            max = cnt
    print(max)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    parents = [0]*N
    for i in range(N-1):
        parents[P[i]-1] += 1
    print(max(parents)+1)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += 1
        p = P[i] - 1
        while p != 0:
            ans += 1
            p = P[p] - 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = max(ans, P[i])
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if p[i] == 1:
            ans = i + 1
            break
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if p[i] == n:
            break
    print(ans)

=======
Suggestion 8

def calc_generation(n,p):
    generation = 0
    while n != 1:
        generation += 1
        n = p[n-1]
    return generation

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if p[i] == 1:
            break
    print(ans)
main()
# 21:20 - 21:29（WA）- 21:35（WA）- 21:38（AC）

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(p)
    ans = 0
    for i in range(1, n):
        if p[i-1] == n:
            ans = i
            break
    print(ans)
main()
