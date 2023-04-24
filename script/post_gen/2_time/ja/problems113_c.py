Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    data = []
    for i in range(m):
        p, y = map(int, input().split())
        data.append([p, y, i])
    data.sort(key=lambda x: x[1])
    p = 1
    x = 1
    result = []
    for d in data:
        if p == d[0]:
            result.append([d[2], p, x])
            x += 1
        else:
            p = d[0]
            x = 1
            result.append([d[2], p, x])
            x += 1
    result.sort(key=lambda x: x[0])
    for r in result:
        print(str(r[1]).zfill(6) + str(r[2]).zfill(6))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    data = []
    for i in range(m):
        p, y = map(int, input().split())
        data.append([i, p, y])
    data.sort(key=lambda x: x[2])
    cnt = [0]*n
    ans = [0]*m
    for i in range(m):
        cnt[data[i][1]-1] += 1
        ans[data[i][0]] = '{:06}'.format(data[i][1])+'{:06}'.format(cnt[data[i][1]-1])
    for i in range(m):
        print(ans[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())

    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())

    #print(P)
    #print(Y)

    Y2 = sorted(Y)
    #print(Y2)

    #print(Y2.index(32))
    #print(Y2.index(12))
    #print(Y2.index(63))

    #print(Y2.index(55))
    #print(Y2.index(77))
    #print(Y2.index(99))

    for i in range(M):
        print(str(P[i]).zfill(6) + str(Y2.index(Y[i]) + 1).zfill(6))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    P_Y = []
    for i in range(M):
        P_Y.append(list(map(int, input().split())))
    P_Y.sort(key=lambda x: x[1])
    #print(P_Y)
    P = [0] * N
    for i in range(M):
        P[P_Y[i][0] - 1] += 1
    #print(P)
    P_Y2 = [0] * M
    for i in range(M):
        P_Y2[i] = [P_Y[i][0], P[P_Y[i][0] - 1]]
    #print(P_Y2)
    P_Y2.sort(key=lambda x: x[0])
    #print(P_Y2)
    P_Y3 = [0] * M
    for i in range(M):
        P_Y3[i] = [P_Y2[i][0], P_Y2[i][1], i + 1]
    #print(P_Y3)
    P_Y3.sort(key=lambda x: x[1])
    #print(P_Y3)
    for i in range(M):
        P_Y3[i] = [P_Y3[i][0], P_Y3[i][2]]
    #print(P_Y3)
    P_Y3.sort(key=lambda x: x[0])
    #print(P_Y3)
    for i in range(M):
        print(str(P_Y3[i][0]).zfill(6) + str(P_Y3[i][1]).zfill(6))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y = sorted(p_y, key=lambda x: x[1])
    p_y = sorted(p_y, key=lambda x: x[0])
    #print(p_y)
    p_y_s = []
    for i in range(len(p_y)):
        p_y_s.append([p_y[i][0], p_y[i][1], i+1])
    #print(p_y_s)
    p_y_s = sorted(p_y_s, key=lambda x: x[1])
    #print(p_y_s)
    ans = []
    for i in range(len(p_y_s)):
        ans.append([p_y_s[i][0], p_y_s[i][2]])
    #print(ans)
    ans = sorted(ans, key=lambda x: x[0])
    #print(ans)
    for i in range(len(ans)):
        print('{:06}{:06}'.format(ans[i][0], ans[i][1]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    D = {}
    for i in range(1, N + 1):
        D[i] = []
    for i in range(M):
        P, Y = map(int, input().split())
        D[P].append([Y, i])
    for i in range(1, N + 1):
        D[i].sort()
        for j in range(len(D[i])):
            D[i][j][0] = str(D[i][j][0]).zfill(6)
            D[i][j][1] = str(D[i][j][1] + 1).zfill(6)
    ans = []
    for i in range(1, N + 1):
        for j in range(len(D[i])):
            ans.append(str(i).zfill(6) + str(D[i][j][1]))
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    p = []
    y = []
    for i in range(m):
        p_,y_ = map(int, input().split())
        p.append(p_)
        y.append(y_)
    p_y = list(zip(p,y))
    p_y.sort()
    #print(p_y)
    count = 0
    for i in range(m):
        count += 1
        p_y[i] = p_y[i] + (count,)
    #print(p_y)
    p_y.sort(key=lambda x: x[1])
    #print(p_y)
    for i in range(m):
        p_y[i] = p_y[i][0:2]
    #print(p_y)
    for i in range(m):
        p_y[i] = p_y[i] + (str(p_y[i][0]).zfill(6) + str(p_y[i][2]).zfill(6),)
    #print(p_y)
    p_y.sort(key=lambda x: x[2])
    #print(p_y)
    for i in range(m):
        print(p_y[i][2])

=======
Suggestion 8

def problem113_c():
    N, M = map(int, input().split())
    city = [[0,0,0] for i in range(M)]
    for i in range(M):
        P, Y = map(int, input().split())
        city[i][0] = P
        city[i][1] = Y
        city[i][2] = i
    city.sort(key=lambda x:x[1])
    pref = [[0,0] for i in range(N)]
    ans = [0 for i in range(M)]
    for i in range(M):
        pref[city[i][0]-1][0] += 1
        pref[city[i][0]-1][1] += 1
        ans[city[i][2]] = str(city[i][0]).zfill(6) + str(pref[city[i][0]-1][1]).zfill(6)
    for i in range(M):
        print(ans[i])

problem113_c()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y_dict = {}
    for p, y in p_y:
        if p in p_y_dict:
            p_y_dict[p].append(y)
        else:
            p_y_dict[p] = [y]
    ans = []
    for p, y in p_y:
        ans.append(str(p).zfill(6) + str(p_y_dict[p].index(y) + 1).zfill(6))
    print(*ans, sep='\n')

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    city = [0]*(n+1)
    for i in range(m):
        p = p_y[i][0]
        y = p_y[i][1]
        city[p] += 1
        print("{:06d}{:06d}".format(p,city[p]))
