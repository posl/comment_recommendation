Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] != X:
            count += 1
        else:
            break
    print(count)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] += 1
    b[x - 1] += 1
    print(b.count(1))

=======
Suggestion 3

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] <= x:
            ans += 1
            x -= a[i]
        else:
            break
    if ans == n and x > 0:
        ans -= 1
    print(ans)

=======
Suggestion 4

def problems228_b():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if x & (1 << i):
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    B = [0] * N
    B[X - 1] = 1
    for i in range(N):
        if B[i] == 1:
            B[A[i]] = 1
    print(sum(B))

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    B = [0] * (N+1)
    B[X] = 1
    for i in range(1, N+1):
        B[A[i]] += B[i]
    print(sum(B))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.insert(0, 0)
    cnt = 0
    for i in range(1, N+1):
        if i == X:
            break
        else:
            cnt += 1
            X = A[X]

    print(cnt)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x-1] + a
    ans = 1
    visited = [False for _ in range(n)]
    visited[0] = True
    i = 0
    while True:
        if visited[a[i]]:
            break
        else:
            visited[a[i]] = True
            ans += 1
            i = a[i]
    print(ans)

=======
Suggestion 9

def friends_learn_the_secret():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 1
    for i in range(1, N):
        if A[X] == 0:
            return count
        else:
            X = A[X]
            count += 1
    return count

=======
Suggestion 10

def main():
    #print("Hello World!")
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A = [x-1 for x in A]
    #print(A)
    #print(N,X)
    #print(A)

    #print(A)
    #print(N,X)
    #print(A)
    #print(A[X-1])
    #print(A[A[X-1]])
    #print(A[A[A[X-1]]])
    #print(A[A[A[A[X-1]]]])
    #print(A[A[A[A[A[X-1]]]]])
    #print(A[A[A[A[A[A[X-1]]]]]])
    #print(A[A[A[A[A[A[A[X-1]]]]]]])
    #print(A[A[A[A[A[A[A[A[X-1]]]]]]]])
    #print(A[A[A[A[A[A[A[A[A[X-1]]]]]]]]])
    #print(A[A[A[A[A[A[A[A[A[A[X-1]]
