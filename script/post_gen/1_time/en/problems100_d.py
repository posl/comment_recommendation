Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X, Y, Z = [], [], []
    for _ in range(N):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    ans = 0
    for i in range(2**3):
        x = [0] * N
        for j in range(N):
            if i & 1:
                x[j] += X[j]
            else:
                x[j] -= X[j]
            if i & 2:
                x[j] += Y[j]
            else:
                x[j] -= Y[j]
            if i & 4:
                x[j] += Z[j]
            else:
                x[j] -= Z[j]
        x.sort(reverse=True)
        ans = max(ans, sum(x[:M]))
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    x = [0] * n
    y = [0] * n
    z = [0] * n
    for i in range(n):
        x[i], y[i], z[i] = map(int, input().split())
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                a = [0] * n
                for l in range(n):
                    if i == 0:
                        a[l] += x[l]
                    else:
                        a[l] -= x[l]
                    if j == 0:
                        a[l] += y[l]
                    else:
                        a[l] -= y[l]
                    if k == 0:
                        a[l] += z[l]
                    else:
                        a[l] -= z[l]
                a.sort(reverse=True)
                b = 0
                for l in range(m):
                    b += a[l]
                ans = max(ans, b)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    x, y, z = [], [], []
    for _ in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)

    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                X = [x[l] if (i + j + k) % 2 == 0 else -x[l] for l in range(N)]
                Y = [y[l] if (i + j + k) % 2 == 0 else -y[l] for l in range(N)]
                Z = [z[l] if (i + j + k) % 2 == 0 else -z[l] for l in range(N)]
                X.sort(reverse=True)
                Y.sort(reverse=True)
                Z.sort(reverse=True)
                ans = max(ans, sum(X[:M]) + sum(Y[:M]) + sum(Z[:M]))
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if (i >> k) & 1:
                    tmp[j] += cake[j][k]
                else:
                    tmp[j] -= cake[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    cakes = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        cakes.append(x + y + z)
        cakes.append(x + y - z)
        cakes.append(x - y + z)
        cakes.append(x - y - z)
    cakes.sort(reverse=True)
    print(sum(cakes[:m]))

main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(2 ** 3):
        score = [0] * N
        for j in range(N):
            for k in range(3):
                if (i >> k) & 1:
                    score[j] += cakes[j][k]
                else:
                    score[j] -= cakes[j][k]
        score.sort(reverse=True)
        ans = max(ans, sum(score[:M]))
    print(ans)

=======
Suggestion 7

def main():
    n, m = [int(i) for i in input().split()]
    cakes = []
    for i in range(n):
        cakes.append([int(i) for i in input().split()])
    ans = 0
    for i in range(2 ** 3):
        tmp = [0] * n
        for j in range(3):
            if (i >> j) & 1:
                for k in range(n):
                    tmp[k] += cakes[k][j]
            else:
                for k in range(n):
                    tmp[k] -= cakes[k][j]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:m]))
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cakes[j][k] * ((i >> k) % 2 * 2 - 1) for k in range(3)]))
        tmp.sort()
        ans = max(ans, sum(tmp[-M:]))
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        A.sort(key=lambda x: sum([(-1)**(i>>j&1)*x[j] for j in range(3)]), reverse=True)
        ans = max(ans, sum([sum([(-1)**(i>>j&1)*A[k][j] for j in range(3)]) for k in range(M)]))
    print(ans)

=======
Suggestion 10

def main():
    N, M = [int(x) for x in input().split()]

    cakes = []
    for i in range(N):
        cakes.append([int(x) for x in input().split()])

    ans = 0
    for i in range(8):
        tmp = 0
        for j in range(N):
            tmp += max(cakes[j][0] if i & 1 == 0 else -cakes[j][0],
                       cakes[j][1] if i & 2 == 0 else -cakes[j][1],
                       cakes[j][2] if i & 4 == 0 else -cakes[j][2])
        ans = max(ans, tmp)

    print(ans)
