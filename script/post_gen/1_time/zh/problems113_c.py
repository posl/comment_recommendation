Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(m)]
    data.sort(key=lambda x: x[1])

    cnt = [0] * (n + 1)
    for p, y in data:
        cnt[p] += 1

    ans = {}
    for p, y in data:
        ans[y] = (str(p).zfill(6) + str(cnt[p]).zfill(6))
        cnt[p] -= 1

    for p, y in data:
        print(ans[y])

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    data = []
    for i in range(m):
        p,y = map(int,input().split())
        data.append([p,y,i])
    data.sort(key=lambda x:x[1])
    ans = []
    cnt = [0]*n
    for i in range(m):
        p,y,i = data[i]
        cnt[p-1] += 1
        ans.append([i,cnt[p-1]])
    ans.sort(key=lambda x:x[0])
    for i in range(m):
        p,x = ans[i]
        print(str(p+1).zfill(6)+str(x).zfill(6))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    py = [list(map(int, input().split())) for _ in range(M)]
    py.sort()
    city = [0] * N
    for i, (p, y) in enumerate(py):
        city[p - 1] += 1
        py[i].append(city[p - 1])
    for p, y, c in py:
        print(str(p).zfill(6) + str(c).zfill(6))

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    # print(p_y)
    ans = [0]*m
    cnt = [0]*n
    for i in range(m):
        cnt[p_y[i][0]-1] += 1
        ans[i] = str(p_y[i][0]).zfill(6) + str(cnt[p_y[i][0]-1]).zfill(6)
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])

    P = [0] * N
    Y = [0] * N
    for i in range(M):
        P[i] = P_Y[i][0]
        Y[i] = P_Y[i][1]

    cnt = [0] * N
    for i in range(M):
        cnt[P[i] - 1] += 1

    ans = [0] * M
    for i in range(M):
        ans[i] = str(P[i]).zfill(6) + str(cnt[P[i] - 1]).zfill(6)
        cnt[P[i] - 1] -= 1

    for i in range(M):
        print(ans[i])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())

    #print(N, M, P, Y)

    #P = [1, 2, 1]
    #Y = [32, 63, 12]
    #N = 2
    #M = 3

    #P = [2, 2, 2]
    #Y = [55, 77, 99]
    #N = 2
    #M = 3

    #print(N, M, P, Y)

    #for i in range(M):
    #    print("%06d%06d" % (P[i], Y[i]))

    #print("")

    #print(N, M, P, Y)

    #print("")

    #for i in range(M):
    #    print("%06d%06d" % (P[i], Y[i]))

    #print("")

    #print(N, M, P, Y)

    #print("")

    #for i in range(M):
    #    print("%06d%06d" % (P[i], Y[i]))

    #print("")

    #print(N, M, P, Y)

    #print("")

    #for i in range(M):
    #    print("%06d%06d" % (P[i], Y[i]))

    #print("")

    #print(N, M, P, Y)

    #print("")

    #for i in range(M):
    #    print("%06d%06d" % (P[i], Y[i]))

    #print("")

    #print(N, M, P, Y)

    #print("")

    #for i in range(M):
    #    print("%06d%06d" % (P[i], Y[i]))

    #print("")

    #print(N, M, P, Y)

    #print("")

    #for i in range(M):
    #    print("%06d%06d" % (P[i], Y[i]))

    #print("")

    #print(N, M, P, Y)

    #print("")

    #for i in range(M):

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    P_Y = [tuple(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    P = [0] * N
    P[P_Y[0][0] - 1] = 1
    c = 1
    for i in range(1, M):
        if P_Y[i - 1][0] != P_Y[i][0]:
            c = 1
        else:
            c += 1
        P[P_Y[i][0] - 1] = c
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6) + str(P[i]).zfill(6))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for i in range(M)]
    PY = sorted(PY, key=lambda x: x[1])
    # print(PY)
    # print(N, M)
    # print(PY)
    city = [0] * N
    for i in range(M):
        city[PY[i][0] - 1] += 1
        PY[i].append(city[PY[i][0] - 1])
    # print(PY)
    for i in range(M):
        print(str(PY[i][0]).zfill(6) + str(PY[i][3]).zfill(6))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: x[1])
    p_y_dict = {}
    for p, y in p_y:
        if p not in p_y_dict:
            p_y_dict[p] = 1
        else:
            p_y_dict[p] += 1
    ans = []
    for p, y in p_y:
        ans.append(str(p).zfill(6) + str(p_y_dict[p]).zfill(6))
        p_y_dict[p] -= 1
    for a in ans:
        print(a)
