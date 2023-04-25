Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    AB = [[a, b] for a, b in zip(A, B)]
    AB = sorted(AB)
    ans = 0
    for i in range(N):
        if M <= AB[i][1]:
            ans += AB[i][0] * M
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A, B = zip(*sorted(zip(A, B)))

    ans = 0
    for i in range(N):
        if M > B[i]:
            M -= B[i]
            ans += A[i]*B[i]
        else:
            ans += A[i]*M
            break

    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = list(zip(A, B))
    C.sort()
    ans = 0
    for a, b in C:
        if M > b:
            M -= b
            ans += a * b
        else:
            ans += a * M
            break
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = [a[i] * b[i] for i in range(n)]
    d = sorted(zip(a, b, c))
    ans = 0
    for i in range(n):
        if m <= d[i][1]:
            ans += d[i][0] * m
            break
        else:
            ans += d[i][2]
            m -= d[i][1]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if M <= b:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    stores = []
    for i in range(N):
        A, B = map(int, input().split())
        stores.append((A, B))
    stores.sort()
    ans = 0
    for i in range(N):
        if M > stores[i][1]:
            ans += stores[i][0] * stores[i][1]
            M -= stores[i][1]
        else:
            ans += stores[i][0] * M
            break
    print(ans)

main()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        ans += min(M, AB[i][1]) * AB[i][0]
        M -= AB[i][1]
        if M <= 0:
            break
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    stores = []
    for i in range(N):
        A, B = map(int, input().split())
        stores.append([A, B])
    stores.sort(key=lambda x: x[0])
    ans = 0
    for A, B in stores:
        if M - B >= 0:
            ans += A * B
            M -= B
        else:
            ans += A * M
            break
    print(ans)

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if M <= b:
            ans += a * M
            break
        else:
            M -= b
            ans += a * b
    print(ans)

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
