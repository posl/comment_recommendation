Synthesizing 10/10 solutions

=======
Suggestion 1

def problems113_c():
    pass

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for i in range(m)]

    p_y.sort(key=lambda x:x[1])

    p = 0
    x = 1
    ans = [0]*m
    for i in range(m):
        if p_y[i][0] != p:
            p = p_y[i][0]
            x = 1
        ans[i] = [p_y[i][0],x]
        x += 1

    ans.sort(key=lambda x:x[0])
    for i in range(m):
        print(str(ans[i][0]).zfill(6)+str(ans[i][1]).zfill(6))

=======
Suggestion 3

def main():
    # 读入数据
    N, M = map(int, input().split())
    PY = []
    for i in range(M):
        PY.append(list(map(int, input().split())))
    # 对数据排序
    PY = sorted(PY, key=lambda x: x[1])
    # 生成ID
    id = []
    for i in range(M):
        # 生成P
        P = str(PY[i][0])
        while len(P) < 6:
            P = '0' + P
        # 生成Y
        Y = str(PY[i][1])
        while len(Y) < 6:
            Y = '0' + Y
        # 生成ID
        id.append(P + Y)
    # 输出ID
    for i in range(M):
        print(id[i])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        city.append(list(map(int, input().split())))
    city.sort(key=lambda x: x[1])
    city_id = [[0 for i in range(2)] for j in range(M)]
    city_id[0][0] = city[0][0]
    city_id[0][1] = 1
    for i in range(1, M):
        if city[i][0] == city_id[i - 1][0]:
            city_id[i][0] = city[i][0]
            city_id[i][1] = city_id[i - 1][1] + 1
        else:
            city_id[i][0] = city[i][0]
            city_id[i][1] = 1
    for i in range(M):
        print(str(city_id[i][0]).zfill(6) + str(city_id[i][1]).zfill(6))

=======
Suggestion 5

def get_id(p, y, i):
    return "%06d%06d" % (p, i)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: (x[0], x[1]))
    city_id = [0] * m
    city_cnt = [0] * (n + 1)
    for i in range(m):
        city_cnt[p_y[i][0]] += 1
        city_id[i] = [p_y[i][0], city_cnt[p_y[i][0]]]
    city_id.sort(key=lambda x: x[1])
    for i in range(m):
        print(str(city_id[i][0]).zfill(6) + str(city_id[i][1]).zfill(6))

=======
Suggestion 7

def getID(p, y):
    return str(p).zfill(6) + str(y).zfill(6)

N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]
PY.sort(key=lambda x: (x[0], x[1]))
ans = [getID(PY[0][0], 1)]
for i in range(1, M):
    if PY[i][0] == PY[i-1][0]:
        ans.append(getID(PY[i][0], len(ans)+1))
    else:
        ans.append(getID(PY[i][0], 1))
for i in ans:
    print(i)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    p_y = []
    for i in range(m):
        p_y.append(list(map(int,input().split())))
    p_y.sort(key=lambda x:x[1])
    p = 1
    x = 1
    for i in range(m):
        if p_y[i][0] == p:
            print("{0}{1}{2}".format(str(p).zfill(6),str(x).zfill(6),str(p_y[i][1]).zfill(6)))
            x+=1
        else:
            p = p_y[i][0]
            x = 1
            print("{0}{1}{2}".format(str(p).zfill(6),str(x).zfill(6),str(p_y[i][1]).zfill(6)))
            x+=1

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x:(x[0], x[1]))
    P_Y_dict = {}
    for i, (P, Y) in enumerate(P_Y):
        P_Y_dict[P] = P_Y_dict.get(P, []) + [(Y, i)]
    for P, Y in P_Y:
        print('{:06d}{:06d}'.format(P, P_Y_dict[P].index((Y, P_Y_dict[P].index((Y, i)))) + 1))

=======
Suggestion 10

def main():
    n,m=map(int,input().split())
    p=[0]*m
    y=[0]*m
    for i in range(m):
        p[i],y[i]=map(int,input().split())
    for i in range(m):
        p[i]=str(p[i])
        y[i]=str(y[i])
    for i in range(m):
        p[i]=p[i].zfill(6)
        y[i]=y[i].zfill(6)
    for i in range(m):
        p[i]=p[i]+y[i]
    p.sort()
    for i in range(m):
        p[i]=p[i][6:]
    for i in range(m):
        print(p[i])
