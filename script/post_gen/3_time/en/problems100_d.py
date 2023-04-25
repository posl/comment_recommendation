Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    x = [0] * N
    y = [0] * N
    z = [0] * N
    for i in range(N):
        x[i], y[i], z[i] = map(int, input().split())
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                a = []
                for l in range(N):
                    if i == 0:
                        a.append(x[l] + y[l] + z[l])
                    else:
                        a.append(-x[l] - y[l] - z[l])
                a.sort(reverse=True)
                if j == 0:
                    ans = max(ans, sum(a[:M]))
                else:
                    ans = max(ans, -sum(a[:M]))
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = []
    Y = []
    Z = []
    for i in range(N):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    ans = 0
    for i in range(8):
        x = sorted([x if i & 1 == 0 else -x for x in X])
        y = sorted([y if i & 2 == 0 else -y for y in Y])
        z = sorted([z if i & 4 == 0 else -z for z in Z])
        ans = max(ans, sum([x[i] + y[i] + z[i] for i in range(M)]))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    cake = []
    for i in range(N):
        cake.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: x[0] if i & 1 == 0 else -x[0])
        cake.sort(key=lambda x: x[1] if i & 2 == 0 else -x[1])
        cake.sort(key=lambda x: x[2] if i & 4 == 0 else -x[2])
        ans = max(ans, sum(cake[j][0] + cake[j][1] + cake[j][2] for j in range(M)))
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for j in range(N):
            s = 0
            for k in range(3):
                if i >> k & 1:
                    s += ABC[j][k]
                else:
                    s -= ABC[j][k]
            tmp.append(s)
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)
main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    cake = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        cake.sort(key=lambda x: sum([-x[j] if i >> j & 1 else x[j] for j in range(3)]), reverse=True)
        ans = max(ans, sum([sum([cake[j][k] if i >> k & 1 else -cake[j][k] for k in range(3)]) for j in range(M)]))
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                cakes.sort(key=lambda x: (-1)**a * x[0] + (-1)**b * x[1] + (-1)**c * x[2], reverse=True)
                ans = max(ans, sum((-1)**a * x[0] + (-1)**b * x[1] + (-1)**c * x[2] for x in cakes[:M]))
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if (i >> k) & 1:
                    tmp[j] += cakes[j][k]
                else:
                    tmp[j] -= cakes[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(8):
        s = [0] * n
        for j in range(n):
            for k in range(3):
                if (i >> k) & 1:
                    s[j] += cakes[j][k]
                else:
                    s[j] -= cakes[j][k]
        s.sort(reverse=True)
        ans = max(ans, sum(s[:m]))

    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    cakes = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        vals = [0] * N
        for j in range(N):
            for k in range(3):
                if i & 1 << k:
                    vals[j] += cakes[j][k]
                else:
                    vals[j] -= cakes[j][k]
        vals.sort(reverse=True)
        ans = max(ans, sum(vals[:M]))
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(n)]
    ans = -1e18
    for i in range(8):
        tmp = 0
        for j in range(n):
            tmp += max([cakes[j][k] if i >> k & 1 else -cakes[j][k] for k in range(3)])
        ans = max(ans, tmp)
    print(ans)
