Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(" ".join(map(str, q)))
main()

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    k = 0
    for i in range(n):
        k += p[i] * (n - i - 1)
    k -= 1
    q = [0] * n
    for i in range(n):
        q[i] = k // (n - i - 1)
        k %= n - i - 1
    for i in range(n):
        for j in range(i):
            if q[j] <= q[i]:
                q[i] += 1
    r = [0] * n
    for i in range(n):
        r[i] = i + 1
    for i in range(n):
        for j in range(i):
            if r[j] <= r[i]:
                r[i] += 1
    for i in range(n):
        r[i] = p[r[i] - 1]
    for i in range(n):
        r[i] = r[q[i]]
    print(*r)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(*q)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [0] + p
    q = [0] * (n + 1)
    for i in range(1, n + 1):
        q[p[i]] = i
    print(' '.join(map(str, q[1:])))

=======
Suggestion 5

def find_min_permutation(n, p):
    # 1. find the largest i, s.t. p[i] > p[i-1]
    i = n - 1
    while i > 0:
        if p[i] > p[i-1]:
            break
        i -= 1
    # 2. find the largest j, s.t. p[j] > p[i-1]
    j = n - 1
    while j > i:
        if p[j] > p[i-1]:
            break
        j -= 1
    # 3. swap p[i-1] and p[j]
    p[i-1], p[j] = p[j], p[i-1]
    # 4. reverse p[i:]
    p[i:] = p[i:][::-1]
    return p

=======
Suggestion 6

def get_next_permutation(a):
    for i in range(len(a)-2, -1, -1):
        if a[i] < a[i+1]:
            target = i
            break
    else:
        return False

    for i in range(len(a)-1, target, -1):
        if a[i] > a[target]:
            a[i], a[target] = a[target], a[i]
            break

    a[target+1:] = reversed(a[target+1:])
    return True

n = int(input())
p = list(map(int, input().split()))
p = [0] + p
q = p[:]

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append(P.index(i+1)+1)
    print(*Q)
