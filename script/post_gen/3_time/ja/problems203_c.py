Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    A.append(10**100)
    B.append(0)
    p = 0
    for i in range(N):
        if K < A[i]:
            break
        p = B[i]
    print(K + p)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ab = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort()
    ans = k
    for i in range(n):
        a, b = ab[i]
        if ans < a:
            break
        ans += b
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    AB = []
    for _ in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort()
    ans = K
    for i in range(N):
        A, B = AB[i]
        if ans < A:
            break
        ans += B
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    friend = []
    for i in range(N):
        A, B = map(int, input().split())
        friend.append([A, B])
    friend.sort()
    for i in range(N):
        if K < friend[i][0]:
            break
        K += friend[i][1]
    print(K)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = k
    for i in range(n):
        if ans < ab[i][0]:
            break
        ans += ab[i][1]
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    ab = []
    for i in range(n):
        a,b = map(int,input().split())
        ab.append([a,b])
    ab.sort()
    for i in range(n):
        a,b = ab[i]
        if k < a:
            break
        else:
            k += b
    print(k)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
        else:
            break
    print(K)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    for a,b in ab:
        if k < a:
            break
        k += b
    print(k)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([10**100, 0])
    current = 0
    for a, b in AB:
        if current + K < a:
            break
        K += b
        current = a
    print(current+K)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    ab.append([10**100+1,0])
    now = 0
    for a,b in ab:
        if a-now>k:
            print(now+k)
            exit()
        else:
            k+=b
            now = a
