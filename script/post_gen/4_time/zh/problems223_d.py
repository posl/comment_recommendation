Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for _ in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    A = [0] * N
    B = [0] * N
    for i in range(M):
        A[AB[i][0]-1] += 1
        B[AB[i][1]-1] += 1
    if max(A) > 1 or max(B) > 1:
        print(-1)
    else:
        P = [0] * N
        for i in range(N):
            if A[i] == 0:
                P[0] = i + 1
        for i in range(N-1):
            for j in range(M):
                if P[i] == AB[j][0]:
                    P[i+1] = AB[j][1]
        for i in range(N):
            print(P[i], end=" ")
        print()

main()

=======
Suggestion 3

def solve(n,m,ab):
    ans = [-1] * n
    for a,b in ab:
        if ans[a-1] == -1:
            ans[a-1] = b
        elif ans[a-1] != b:
            return [-1]
    if ans[0] == -1:
        ans[0] = 1
    for i in range(1,n):
        if ans[i] == -1:
            ans[i] = ans[i-1] + 1
    return ans

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def find_next(n, m, a, b):
    next = [0] * (n+1)
    for i in range(1, n+1):
        next[i] = i
    for i in range(m):
        if next[a[i]] > next[b[i]]:
            next[a[i]], next[b[i]] = next[b[i]], next[a[i]]
    return next
