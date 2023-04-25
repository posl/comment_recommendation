Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, k = map(int, input().split())
    f = [set() for _ in range(n)]
    b = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        f[a - 1].add(b - 1)
        f[b - 1].add(a - 1)
    for _ in range(k):
        c, d = map(int, input().split())
        b[c - 1].add(d - 1)
        b[d - 1].add(c - 1)
    ans = [0] * n
    for i in range(n):
        ans[i] = n - len(f[i]) - 1 - len(b[i])
    for i in range(n):
        for j in f[i]:
            if i in f[j]:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(n):
        print(ans[i], end=" ")
    print()

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    friend = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a-1].add(b-1)
        friend[b-1].add(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        block[c-1].add(d-1)
        block[d-1].add(c-1)
    for i in range(N):
        ans = N - len(friend[i]) - 1
        for j in friend[i]:
            ans -= len(friend[j] & block[i])
        print(ans, end=' ')

=======
Suggestion 3

def solve():
    N, M, K = map(int, input().split())
    friends = [set() for _ in range(N)]
    blocks = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a - 1].add(b - 1)
        friends[b - 1].add(a - 1)
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c - 1].add(d - 1)
        blocks[d - 1].add(c - 1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friends[i]) - 1
        for j in friends[i]:
            ans[i] -= len(friends[j] & blocks[i])
    for i in range(N):
        print(ans[i], end=" ")

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    friend = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friend[A].add(B)
        friend[B].add(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        block[C].add(D)
        block[D].add(C)
    for i in range(N):
        ans = N - len(friend[i]) - 1
        for j in friend[i]:
            ans -= len(friend[j] & block[i])
        print(ans, end=' ')

=======
Suggestion 5

def main():
    N, M, K = list(map(int, input().split()))
    friend = [[0 for i in range(N)] for j in range(N)]
    block = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        a, b = list(map(int, input().split()))
        friend[a - 1][b - 1] = 1
        friend[b - 1][a - 1] = 1
    for i in range(K):
        c, d = list(map(int, input().split()))
        block[c - 1][d - 1] = 1
        block[d - 1][c - 1] = 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            if friend[i][j] == 1:
                cnt += 1
        for j in range(N):
            if block[i][j] == 1:
                cnt += 1
        print(N - cnt - 1, end = " ")

=======
Suggestion 6

def main():
    # Input
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K

    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    
    # Solve
    # Initialize
    # Each user has no friend candidate
    ans = [0] * N
    # Each user has no friend
    friends = [set() for i in range(N)]
    # Each user has no blockship
    blockships = [set() for i in range(N)]
    
    # Input friends
    for i in range(M):
        a = A[i] - 1
        b = B[i] - 1
        # Add friendship
        friends[a].add(b)
        friends[b].add(a)
    
    # Input blockships
    for i in range(K):
        c = C[i] - 1
        d = D[i] - 1
        # Add blockship
        blockships[c].add(d)
        blockships[d].add(c)
    
    # Calculate friend candidates
    # For each user
    for i in range(N):
        # Calculate the number of users who are not friends of the user
        # and who are not blocked by the user
        ans[i] = N - len(friends[i]) - 1
        # Calculate the number of users who are blocked by the user
        for j in blockships[i]:
            # If the user is blocked by the user
            if i in friends[j]:
                # The user is not a friend candidate
                ans[i] -= 1
    
    # Output
    print(*ans)
    
    return

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    block = [[] for _ in range(N)]
    friend = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        block[c-1].append(d-1)
        block[d-1].append(c-1)

    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friend[i]) - 1
        for j in block[i]:
            if j in friend[i]:
                ans[i] -= 1
    for i in range(N):
        for j in friend[i]:
            if i < j:
                ans[i] -= 1
                ans[j] -= 1
    print(*ans)

=======
Suggestion 8

def main():
    # Input
    N, M, K = map(int, input().split())
    friends = [set() for _ in range(N)]
    blocks = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friends[A].add(B)
        friends[B].add(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        blocks[C].add(D)
        blocks[D].add(C)

    # Solve
    ans = [0] * N
    for i in range(N):
        ans[i] = len(friends[i])
    for i in range(N):
        for j in friends[i]:
            if i in blocks[j]:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        ans[i] -= 1

    # Output
    print(*ans)

=======
Suggestion 9

def main():
    # Read the data
    N, M, K = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(K):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    # Solve the problem
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1
    for i in range(M):
        ans[A[i] - 1] -= 1
        ans[B[i] - 1] -= 1
    for i in range(K):
        if ans[C[i] - 1] > 0 and ans[D[i] - 1] > 0:
            ans[C[i] - 1] -= 1
            ans[D[i] - 1] -= 1
    for i in range(N):
        for j in range(M):
            if A[j] == i + 1 or B[j] == i + 1:
                ans[i] -= 1
    # Print the answer
    for i in range(N):
        print(ans[i], end = " ")
    print()

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
