Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = []
    y = []
    z = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                s = []
                for l in range(n):
                    s.append(x[l] * (2 * i - 1) + y[l] * (2 * j - 1) + z[l] * (2 * k - 1))
                s.sort(reverse=True)
                ans = max(ans, sum(s[:m]))
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        x, y, z = map(int, input().split())
        cakes.append([x, y, z])
    ans = 0
    for i in range(8):
        cakes.sort(key=lambda x: (x[0] * (-1) ** (i & 1) + x[1] * (-1) ** (i >> 1 & 1) + x[2] * (-1) ** (i >> 2 & 1)))
        beauty = sum([cake[0] for cake in cakes[:M]])
        tastiness = sum([cake[1] for cake in cakes[:M]])
        popularity = sum([cake[2] for cake in cakes[:M]])
        ans = max(ans, abs(beauty) + abs(tastiness) + abs(popularity))
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())

    cakes = []
    for i in range(N):
        x, y, z = map(int, input().split())
        cakes.append((x, y, z))

    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for j in range(N):
            val = 0
            for k in range(3):
                if i >> k & 1:
                    val += cakes[j][k]
                else:
                    val -= cakes[j][k]
            tmp.append(val)
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))

    print(ans)

=======
Suggestion 4

def main():
    N, M = list(map(int, input().split()))
    xyz = []
    for i in range(N):
        x, y, z = list(map(int, input().split()))
        xyz.append([x, y, z])
    ans = 0
    for i in range(2 ** 3):
        op = [1, 1, 1]
        for j in range(3):
            if i & (2 ** j) != 0:
                op[j] = -1
        xyz.sort(key=lambda x: op[0] * x[0] + op[1] * x[1] + op[2] * x[2], reverse=True)
        t = 0
        for j in range(M):
            t += op[0] * xyz[j][0] + op[1] * xyz[j][1] + op[2] * xyz[j][2]
        ans = max(ans, abs(t))
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        xyz.sort(key=lambda x: (-(x[0] * ((i >> 2) % 2 * 2 - 1) + x[1] * ((i >> 1) % 2 * 2 - 1) + x[2] * (i % 2 * 2 - 1))))
        tmp = 0
        for j in range(M):
            tmp += xyz[j][0] * ((i >> 2) % 2 * 2 - 1) + xyz[j][1] * ((i >> 1) % 2 * 2 - 1) + xyz[j][2] * (i % 2 * 2 - 1)
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        xyz.sort(reverse=True, key=lambda x:sum([x[i] for i in range(3)]))
        tmp = 0
        for j in range(M):
            tmp += sum([xyz[j][i] for i in range(3)])
        ans = max(ans, abs(tmp))
    print(ans)

=======
Suggestion 7

def main():
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans=0
    for i in range(2**3):
        b=[]
        for j in range(n):
            tmp=0
            for k in range(3):
                if (i>>k)&1:
                    tmp+=a[j][k]
                else:
                    tmp-=a[j][k]
            b.append(tmp)
        b.sort(reverse=True)
        tmp=0
        for j in range(m):
            tmp+=b[j]
        ans=max(ans,tmp)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    for i in range(8):
        s = 0
        for j in range(N):
            t = 0
            for k in range(3):
                t += xyz[j][k] * (-1)**((i>>k) & 1)
            s += t
        ans = max(ans, abs(s))
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    xyz = []
    for i in range(n):
        xyz.append(list(map(int, input().split())))
    print(max([sum(sorted([sum([abs(xyz[i][j]) for i in range(n) if (i >> k) & 1]) for k in range(3)], reverse=True)[:m]) for j in range(3)]))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    cakes = [list(map(int, input().split())) for i in range(n)]

    # 0: -x, 1: +x
    # 0: -y, 1: +y
    # 0: -z, 1: +z
    signs = [[0, 1] for i in range(8)]

    ans = 0
    for i in range(8):
        cakes.sort(key=lambda x: (x[0] * signs[i][0] + x[1] * signs[i][1] + x[2] * signs[i][2]), reverse=True)
        ans = max(ans, sum(map(lambda x: x[0] * signs[i][0] + x[1] * signs[i][1] + x[2] * signs[i][2], cakes[:m])))
    print(ans)
