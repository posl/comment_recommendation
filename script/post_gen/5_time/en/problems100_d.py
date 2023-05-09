Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x, y, z = [], [], []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans = 0
    for i in range(1 << 3):
        x1, y1, z1 = [], [], []
        for j in range(n):
            if i & 1:
                x1.append(x[j])
            else:
                x1.append(-x[j])
            if i & 2:
                y1.append(y[j])
            else:
                y1.append(-y[j])
            if i & 4:
                z1.append(z[j])
            else:
                z1.append(-z[j])
        x1.sort(reverse=True)
        y1.sort(reverse=True)
        z1.sort(reverse=True)
        ans = max(ans, sum(x1[:m]) + sum(y1[:m]) + sum(z1[:m]))
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    cakes = []
    for _ in range(n):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**3):
        cakes.sort(reverse=True, key=lambda x: (x[0]*((i>>0)&1)*2-1) + (x[1]*((i>>1)&1)*2-1) + (x[2]*((i>>2)&1)*2-1))
        ans = max(ans, sum(map(lambda x: abs(x[0])+abs(x[1])+abs(x[2]), cakes[:m])))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        sign = [-1, -1, -1]
        if i & 1:
            sign[0] = 1
        if i & 2:
            sign[1] = 1
        if i & 4:
            sign[2] = 1
        cakes.sort(key=lambda x: sum([sign[j] * x[j] for j in range(3)]), reverse=True)
        tmp = 0
        for j in range(M):
            tmp += sum([sign[k] * cakes[j][k] for k in range(3)])
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    XYZ = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(2 ** 3):
        XYZ.sort(key=lambda x: sum(x[j] * (-1 if (i >> j) & 1 else 1) for j in range(3)))
        ans = max(ans, sum(sum(x[j] * (-1 if (i >> j) & 1 else 1) for j in range(3)) for x in XYZ[:M]))

    print(ans)

=======
Suggestion 5

def main():
    N,M = list(map(int,input().split()))
    X = []
    Y = []
    Z = []
    for i in range(N):
        x,y,z = list(map(int,input().split()))
        X.append(x)
        Y.append(y)
        Z.append(z)
    ans = 0
    for i in range(2**3):
        Xp = []
        Yp = []
        Zp = []
        for j in range(3):
            if ((i >> j) & 1):
                Xp.append(X[j])
                Yp.append(Y[j])
                Zp.append(Z[j])
            else:
                Xp.append(-X[j])
                Yp.append(-Y[j])
                Zp.append(-Z[j])
        Xp.sort(reverse=True)
        Yp.sort(reverse=True)
        Zp.sort(reverse=True)
        ans = max(ans,sum(Xp[:M])+sum(Yp[:M])+sum(Zp[:M]))
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(2**3):
        xyz.sort(key=lambda x: sum([x[k] * (-1)**((i>>k)&1) for k in range(3)]), reverse=True)
        ans = max(ans, sum([sum([x[k] * (-1)**((i>>k)&1) for k in range(3)]) for x in xyz[:m]]))

    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    cakes.sort(reverse=True, key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]))
    ans = 0
    for i in range(M):
        ans += abs(cakes[i][0]) + abs(cakes[i][1]) + abs(cakes[i][2])
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(8):
        xyz.sort(reverse=True, key=lambda x: (x[0]*(-1)**(i&1), x[1]*(-1)**((i>>1)&1), x[2]*(-1)**((i>>2)&1)))
        tmp = [0,0,0]
        for j in range(m):
            tmp[0] += xyz[j][0]
            tmp[1] += xyz[j][1]
            tmp[2] += xyz[j][2]
        ans = max(ans, abs(tmp[0]) + abs(tmp[1]) + abs(tmp[2]))
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    #print(cakes)
    max = 0
    for i in range(1 << 3):
        #print(i)
        tmp = []
        for j in range(N):
            tmp.append(cakes[j][0] * ((-1) ** ((i >> 0) & 1)) + cakes[j][1] * ((-1) ** ((i >> 1) & 1)) + cakes[j][2] * ((-1) ** ((i >> 2) & 1)))
        tmp.sort(reverse=True)
        #print(tmp)
        sum = 0
        for j in range(M):
            sum += tmp[j]
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 10

def max_value():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        cakes.sort(key=lambda x: (x[0] * (-1) ** (i // 4 % 2), x[1] * (-1) ** (i // 2 % 2), x[2] * (-1) ** (i % 2)))
        ans = max(ans, sum(sum(i) for i in zip(*cakes[:m])))
    print(ans)

max_value()
