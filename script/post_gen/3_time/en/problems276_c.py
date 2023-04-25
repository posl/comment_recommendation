Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(' '.join(map(str, q)))

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i, p in enumerate(P):
        Q[p-1] = i+1
    print(*Q)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    q = [0] * (n + 1)
    for i in range(1, n + 1):
        q[p[i]] = i
    print(*q[1:])

=======
Suggestion 6

def reverseList(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return a

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    s = sorted(p)
    for i in range(n):
        p[i] = s.index(p[i])+1
    print(*p)

=======
Suggestion 8

def getPermutations(N, P):
    permutations = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if P[j-1] == i:
                permutations.append(j)
    return permutations

=======
Suggestion 9

def get_permutation(n, k):
    ans = []
    for i in range(1, n+1):
        ans.append(i)
    for i in range(k-1):
        for j in range(n-1, 0, -1):
            if ans[j-1] < ans[j]:
                break
        for k in range(n-1, j-1, -1):
            if ans[j-1] < ans[k]:
                break
        ans[j-1], ans[k] = ans[k], ans[j-1]
        ans[j:] = ans[j:][::-1]
    return ans

n = int(input())
p = list(map(int, input().split()))
k = 1
for i in range(n):
    k += (p[i] - 1) * math.factorial(n - i - 1)
print(*get_permutation(n, k))
