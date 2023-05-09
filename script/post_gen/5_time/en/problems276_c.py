Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(*q)

=======
Suggestion 2

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(*q)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i + 1
    print(*Q)

=======
Suggestion 4

def solve():
    n=int(input())
    p=list(map(int,input().split()))
    p.insert(0,0)
    q=[0]*(n+1)
    for i in range(1,n+1):
        q[p[i]]=i
    print(*q[1:])
solve()

=======
Suggestion 5

def get_next_permutation(perm):
    n = len(perm)
    i = n - 1
    while i > 0 and perm[i - 1] >= perm[i]:
        i -= 1
    if i <= 0:
        return []
    j = n - 1
    while perm[j] <= perm[i - 1]:
        j -= 1
    perm[i - 1], perm[j] = perm[j], perm[i - 1]
    perm[i : ] = perm[n - 1 : i - 1 : -1]
    return perm

n = int(input())
p = list(map(int, input().split()))
p = get_next_permutation(p)
print(" ".join(map(str, p)))

=======
Suggestion 6

def lexico_smallest_permutation(n, p):
    p = p.split()
    p = list(map(int, p))
    q = []
    for i in range(n):
        q.append(p.index(i+1)+1)
    q = list(map(str, q))
    return ' '.join(q)
