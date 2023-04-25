Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    ans = 0
    for i in range(N, 0, -1):
        if P[i] == 1:
            ans = i
            break
        else:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1,0,-1):
        ans = max(ans, p[i-1])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    count = 0
    while N != 1:
        N = P[N]
        count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    d = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        d[i] = d[p[i]] + 1
    print(max(d))

=======
Suggestion 5

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    G = [0] * (N + 1)
    for i in range(1, N + 1):
        G[i] = G[P[i]] + 1
    print(max(G))

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    g = 0
    for i in range(n, 0, -1):
        if p[i] == 1:
            g += 1
            break
        else:
            g += 1
            i = p[i]
    print(g)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        temp = 0
        while p[i] != 1:
            p[i] = p[p[i] - 2]
            temp += 1
        ans = max(ans, temp)
    print(ans + 1)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    print(solve(n, p))

=======
Suggestion 9

def get_generation(n, p):
    if p[n] == 1:
        return 1
    else:
        return get_generation(n, p) + 1

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, None)
    print(get_generation(n, p))
