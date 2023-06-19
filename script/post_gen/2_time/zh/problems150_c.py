Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    # print(p,q)
    a = 0
    b = 0
    for i in range(n):
        a += p[i]*(n-i)
        b += q[i]*(n-i)
    print(abs(a-b))

=======
Suggestion 2

def solve(n, p, q):
    a, b = 0, 0
    for i in range(n):
        a = a * (n - i) + p[i] - 1
        b = b * (n - i) + q[i] - 1
    return abs(a - b)

=======
Suggestion 3

def permutation(n, p, q):
    count = 0
    for i in range(n):
        for j in range(n):
            if p[i] == q[j]:
                count += abs(i-j)
    return count

=======
Suggestion 4

def dfs(p,q):
    if len(p) == 0:
        return 0
    else:
        return dfs(p[1:],q[1:]) + (p[0] - q[0])**2

=======
Suggestion 5

def calc(n, p, q):
    p = [i-1 for i in p]
    q = [i-1 for i in q]
    p = [p.index(i) for i in range(n)]
    q = [q.index(i) for i in range(n)]
    return abs(p.index(0) - q.index(0))

=======
Suggestion 6

def permutation(n):
    if n == 1:
        return [[1]]
    else:
        result = []
        for i in range(n):
            for j in permutation(n-1):
                result.append(j[:i]+[n]+j[i:])
        return result

=======
Suggestion 7

def permutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in permutation(n-1)] + [p + [n] for p in permutation(n-1)]

=======
Suggestion 8

def main():
    # read input
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    # process
    # 1. find the order of p and q
    # 2. find the difference of order of p and q
    # 3. print the difference
    print(abs(order(p) - order(q)))

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(abs(p.index(1)-q.index(1)))

=======
Suggestion 10

def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))

    def solve(n, p, q):
        def dfs(n, a, b, c):
            if n == 0:
                return b, c
            k = a.index(n)
            return dfs(n-1, a[:k]+a[k+1:], b*k+c, c+1)
        return abs(dfs(n, list(range(1, n+1)), 0, 0)[0] - dfs(n, list(range(1, n+1)), 0, 0)[1])
    print(solve(n, p, q))
