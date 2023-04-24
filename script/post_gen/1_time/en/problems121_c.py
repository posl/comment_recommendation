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

    AB = sorted(zip(A, B))
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
        if M < B[i]:
            ans += A[i] * M
            break
        else:
            ans += A[i] * B[i]
            M -= B[i]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = (list(t) for t in zip(*sorted(zip(A, B))))
    ans = 0
    for i in range(N):
        if M - B[i] < 0:
            ans += A[i] * M
            break
        else:
            M -= B[i]
            ans += A[i] * B[i]
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # sort by price
    idx = sorted(range(N), key=lambda k: A[k])
    A = [A[i] for i in idx]
    B = [B[i] for i in idx]

    ans = 0
    for i in range(N):
        if B[i] >= M:
            ans += A[i] * M
            break
        else:
            ans += A[i] * B[i]
            M -= B[i]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    stores = []
    for _ in range(N):
        A, B = map(int, input().split())
        stores.append((A, B))
    stores.sort()
    ans = 0
    for A, B in stores:
        if M <= B:
            ans += A * M
            break
        else:
            ans += A * B
            M -= B
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if AB[i][1] < M:
            M -= AB[i][1]
            ans += AB[i][0] * AB[i][1]
        else:
            ans += AB[i][0] * M
            break
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for A, B in AB:
        if M > B:
            ans += A * B
            M -= B
        else:
            ans += A * M
            break
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for a, b in AB:
        if b >= M:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(N)]
    store.sort()

    ans = 0
    for i in range(N):
        if M - store[i][1] >= 0:
            ans += store[i][0] * store[i][1]
            M -= store[i][1]
        else:
            ans += store[i][0] * M
            break
    print(ans)

=======
Suggestion 10

def main():
    N,M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a,b in AB:
        if M <= b:
            ans += a*M
            break
        else:
            ans += a*b
            M -= b
    print(ans)
