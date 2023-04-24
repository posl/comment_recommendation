Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
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
    for i in range(N):
        print(N-1-M-K, end=" ")
    print()

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        blocks[c].append(d)
        blocks[d].append(c)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friends[i]) - 1
        for j in friends[i]:
            if i in friends[j]:
                ans[i] -= 1
        for j in blocks[i]:
            if j in friends[i]:
                ans[i] -= 1
    print(*ans)

=======
Suggestion 3

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
        ans[i] = n - len(f[i]) - 1
    for i in range(n):
        for j in f[i]:
            ans[i] -= len(f[j] & b[i])
    print(*ans)

=======
Suggestion 4

def main():
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
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1 - len(friends[i]) - len(blocks[i])
        for j in friends[i]:
            if i in blocks[j]:
                ans[i] -= 1
        ans[i] -= 1
    print(*ans)

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    friends = [[0] * N for _ in range(N)]
    blocks = [[0] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A - 1][B - 1] = 1
        friends[B - 1][A - 1] = 1
    for _ in range(K):
        C, D = map(int, input().split())
        blocks[C - 1][D - 1] = 1
        blocks[D - 1][C - 1] = 1
    for i in range(N):
        blocks[i][i] = 1
    for i in range(N):
        for j in range(N):
            if friends[i][j] == 1:
                for k in range(N):
                    blocks[i][k] = 1
                    blocks[j][k] = 1
    for i in range(N):
        for j in range(N):
            if friends[i][j] == 1:
                blocks[i][j] = 0
    for i in range(N):
        print(sum(blocks[i]) - 1, end=' ')
    print()

=======
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    friend = [set() for i in range(n)]
    block = [set() for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friend[a].add(b)
        friend[b].add(a)
    for i in range(k):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        block[c].add(d)
        block[d].add(c)
    ans = [0] * n
    for i in range(n):
        ans[i] = n - len(friend[i]) - 1
        for j in friend[i]:
            if i in block[j]:
                ans[i] -= 1
        if i in block[i]:
            ans[i] += 1
    print(*ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    friends = [[0] * N for _ in range(N)]
    blocks = [[0] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A - 1][B - 1] = 1
        friends[B - 1][A - 1] = 1
    for _ in range(K):
        C, D = map(int, input().split())
        blocks[C - 1][D - 1] = 1
        blocks[D - 1][C - 1] = 1
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1 - sum(friends[i]) - sum(blocks[i])
    for i in range(N):
        for j in range(N):
            if friends[i][j] == 1 and blocks[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        if friends[i][i] == 1:
            ans[i] -= 1
    for i in range(N):
        print(ans[i], end=' ')
    print()

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    block = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a].append(b)
        friends[b].append(a)
    for _ in range(K):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        block[c].append(d)
        block[d].append(c)

    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friends[i]) - 1

    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        q = [i]
        while q:
            x = q.pop()
            for y in friends[x]:
                if visited[y]:
                    continue
                visited[y] = True
                q.append(y)
                ans[i] -= 1
                ans[y] -= 1
                for z in block[y]:
                    if visited[z]:
                        continue
                    ans[z] -= 1

    print(*ans)

main()

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocked = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A - 1].append(B - 1)
        friends[B - 1].append(A - 1)
    for _ in range(K):
        C, D = map(int, input().split())
        blocked[C - 1].append(D - 1)
        blocked[D - 1].append(C - 1)
    result = [0] * N
    for i in range(N):
        result[i] = N - len(friends[i]) - 1
        for j in friends[i]:
            if i in friends[j]:
                result[i] -= 1
        for j in blocked[i]:
            if j in friends[i]:
                result[i] -= 1
    print(*result)

=======
Suggestion 10

def  main():
    N, M, K =  map ( int ,  input (). split ())
    A = []
    B = []
    C = []
    D = []
     for  i  in   range (M):
        a, b =  map ( int ,  input (). split ())
        A.append(a)
        B.append(b)
     for  i  in   range (K):
        c, d =  map ( int ,  input (). split ())
        C.append(c)
        D.append(d)
    friends =  dict ()
     for  i  in   range (N):
        friends[i + 1] = []
     for  i  in   range (M):
        friends[A[i]].append(B[i])
        friends[B[i]].append(A[i])
    blocks =  dict ()
     for  i  in   range (N):
        blocks[i + 1] = []
     for  i  in   range (K):
        blocks[C[i]].append(D[i])
        blocks[D[i]].append(C[i])
    ans =  [0] * N
     for  i  in   range (N):
        ans[i] =  len (friends[i + 1]) +  len (blocks[i + 1])
        ans[i] = N - ans[i] - 1
         for  j  in  friends[i + 1]:
            ans[j - 1] -= 1
             if  i + 1  in  blocks[j]:
                ans[j - 1] += 1
     for  i  in  ans:
        print (i,  end = ' ' )
    print ()
