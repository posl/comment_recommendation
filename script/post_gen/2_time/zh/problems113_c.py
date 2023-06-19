Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    citys = []
    for i in range(m):
        p, y = map(int, input().split())
        citys.append([i, p, y])
    citys.sort(key=lambda x: (x[1], x[2]))
    ans = {}
    for i in range(m):
        ans[citys[i][0]] = str(citys[i][1]).zfill(6) + str(i + 1).zfill(6)
    for i in range(m):
        print(ans[i])

=======
Suggestion 2

def main():
    N,M = map(int, input().split())
    city = [list(map(int, input().split())) for i in range(M)]
    city = sorted(city, key=lambda x:x[1])
    cnt = 0
    ans = [0]*M
    for i in range(M):
        if i == 0:
            cnt += 1
            ans[i] = str(city[i][0]).zfill(6)+str(cnt).zfill(6)
        else:
            if city[i-1][0] == city[i][0]:
                cnt += 1
                ans[i] = str(city[i][0]).zfill(6)+str(cnt).zfill(6)
            else:
                cnt = 1
                ans[i] = str(city[i][0]).zfill(6)+str(cnt).zfill(6)
    for i in range(M):
        print(ans[i])

=======
Suggestion 3

def main():
    n,m = map(int, input().split())
    data = []
    for i in range(m):
        p,y = map(int, input().split())
        data.append([p,y,i])
    data.sort(key=lambda x:x[1])
    ans = [0] * m
    cnt = [0] * (n+1)
    for i in range(m):
        p,y,idx = data[i]
        cnt[p] += 1
        ans[idx] = str(p).zfill(6) + str(cnt[p]).zfill(6)
    for i in range(m):
        print(ans[i])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    P_Y_dict = {}
    for i in range(M):
        P_Y_dict[P_Y[i][0]] = P_Y_dict.get(P_Y[i][0], []) + [i]
    ans = [0] * M
    for i in range(1, N + 1):
        for j in range(len(P_Y_dict[i])):
            ans[P_Y_dict[i][j]] = str(i).zfill(6) + str(j + 1).zfill(6)
    for i in range(M):
        print(ans[i])

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    pm = []
    for i in range(m):
        p,y = map(int,input().split())
        pm.append([p,y])
    pm.sort(key=lambda x:x[1])
    print(pm)

    for i in range(m):
        print("{:06}{:06}".format(pm[i][0],i+1))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: x[1])
    p = {}
    for i in range(m):
        if p_y[i][0] not in p:
            p[p_y[i][0]] = 1
        else:
            p[p_y[i][0]] += 1
        p_y[i].append(p[p_y[i][0]])
    p_y.sort(key=lambda x: x[2])
    for i in range(m):
        print(str(p_y[i][0]).zfill(6) + str(p_y[i][3]).zfill(6))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for i in range(M)]
    PY.sort(key=lambda x: x[1])
    city = [0] * (N + 1)
    for p, y in PY:
        city[p] += 1
        print("{:06d}{:06d}".format(p, city[p]))

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    P_Y = [list(map(int,input().split())) for i in range(M)]
    P_Y.sort(key=lambda x:x[1])
    city = {i:[] for i in range(1,N+1)}
    for p,y in P_Y:
        city[p].append(y)
    for p,y in P_Y:
        print("%06d%06d"%(p,city[p].index(y)+1))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    P_Y = []
    for i in range(M):
        P_Y.append(list(map(int, input().split())))
    P_Y.sort(key=lambda x: x[1])
    ID = []
    for i in range(M):
        ID.append([P_Y[i][0], i+1, 1])
    ID.sort(key=lambda x: x[0])
    for i in range(M):
        ID[i][2] = str(ID[i][1]).zfill(6)
        ID[i][0] = str(ID[i][0]).zfill(6)
    for i in range(M):
        print(ID[i][0] + ID[i][2])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    city = [0 for _ in range(N + 1)]
    for i in range(M):
        city[P_Y[i][0]] += 1
        P_Y[i].append(city[P_Y[i][0]])
    P_Y.sort()
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6) + str(P_Y[i][3]).zfill(6))
