Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    count = 0
    for i in range(N):
        count += B.count(C[A[i]-1])
    print(count)

=======
Suggestion 3

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    C = [i-1 for i in C]
    D = {}
    for i in C:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    ans = 0
    for i in range(N):
        if B[i] in D:
            ans += D[B[i]]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    d = [0] * (n + 1)
    for i in range(n):
        d[c[i]] += 1

    e = [0] * (n + 1)
    for i in range(1, n + 1):
        e[b[c[i - 1] - 1]] += 1

    ans = 0
    for i in range(1, n + 1):
        ans += d[a[i - 1]] * e[i]

    print(ans)

=======
Suggestion 5

def count_same_num(N, A, B, C):
    # 暴力法
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                count += 1
    return count

=======
Suggestion 6

def problem202c():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    d = [0] * (n + 1)
    for i in range(n):
        d[b[c[i] - 1]] += 1

    ans = 0
    for i in range(n):
        ans += d[a[i]]

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [0] * (N + 1)
    for i in range(N):
        D[B[C[i]]] += 1
    print(sum([D[A[i]] for i in range(N)]))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))

    d = [0] * n
    for i in range(n):
        d[b[c[i]]] += 1

    ans = 0
    for i in range(n):
        ans += d[a[i]]

    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int,input().split()))
    #print(n,a,b,c)
    d = [0] * n
    for i in range(n):
        d[c[i]-1] += 1
    #print(d)
    e = [0] * n
    for i in range(n):
        e[b[c[i]-1]-1] += 1
    #print(e)
    sum = 0
    for i in range(n):
        sum += d[i] * e[i]
    print(sum)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    from collections import Counter
    c = Counter(c)
    ans = 0
    for i in range(1, n+1):
        ans += c[b[a[i-1]-1]]
    print(ans)
