Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    P_Y = list(zip(P, Y))
    P_Y.sort(key=lambda x: x[1])
    P_Y.sort(key=lambda x: x[0])
    P_Y_dict = {}
    for i in range(M):
        if P_Y[i][0] in P_Y_dict:
            P_Y_dict[P_Y[i][0]] += 1
        else:
            P_Y_dict[P_Y[i][0]] = 1
        P_Y[i] = (str(P_Y[i][0]).zfill(6), str(P_Y_dict[P_Y[i][0]]).zfill(6))
    for i in range(M):
        print(P_Y[i][0] + P_Y[i][1])

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    print(p)
    print(y)
    return

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    prefecture = [[] for i in range(n)]
    for i in range(m):
        p, y = map(int, input().split())
        prefecture[p-1].append([i, y])
    for i in range(n):
        prefecture[i].sort(key=lambda x: x[1])
        for j in range(len(prefecture[i])):
            prefecture[i][j].append(str(i+1).zfill(6))
            prefecture[i][j].append(str(j+1).zfill(6))
    for i in range(n):
        for j in range(len(prefecture[i])):
            print(''.join(prefecture[i][j][2:4]))

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    d = {}
    for i in range(m):
        p,y = map(int, input().split())
        if p not in d:
            d[p] = []
        d[p].append((i,y))
    for k in d.keys():
        d[k] = sorted(d[k], key=lambda x:x[1])
    r = [0]*m
    for k in d.keys():
        for i in range(len(d[k])):
            r[d[k][i][0]] = str(k).zfill(6) + str(i+1).zfill(6)
    for i in range(m):
        print(r[i])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y = sorted(p_y, key=lambda x: x[1])
    p_y_dict = {}
    for p, y in p_y:
        if p not in p_y_dict:
            p_y_dict[p] = 1
        else:
            p_y_dict[p] += 1
    ans = []
    for p, y in p_y:
        ans.append('{0:06d}{1:06d}'.format(p, p_y_dict[p]))
        p_y_dict[p] += 1
    print(*ans, sep='\n')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cities = []
    prefectures = [0] * N
    for i in range(M):
        P, Y = map(int, input().split())
        cities.append([P, Y, i])
        prefectures[P - 1] += 1
    cities.sort(key=lambda x: x[1])
    ids = [0] * M
    for i in range(M):
        ids[cities[i][2]] = str(cities[i][0]).zfill(6) + str(prefectures[cities[i][0] - 1]).zfill(6)
        prefectures[cities[i][0] - 1] -= 1
    for i in range(M):
        print(ids[i])

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    city = []
    for i in range(m):
        p,y = map(int,input().split())
        city.append([p,y,i])
    city = sorted(city,key=lambda x:(x[0],x[1]))
    ans = []
    for i in range(m):
        p,y,i = city[i]
        ans.append([i,(str(p).zfill(6)+str(i+1).zfill(6))])
    ans = sorted(ans,key=lambda x:x[0])
    for i in range(m):
        print(ans[i][1])

=======
Suggestion 8

def main():
    # Get input here
    N, M = map(int, input().split())
    py = []
    for i in range(M):
        p, y = map(int, input().split())
        py.append((p, y, i))
    # Calculate desired output below
    py.sort(key=lambda x:(x[0], x[1]))
    p = 0
    x = 1
    ans = []
    for i in range(M):
        if p == py[i][0]:
            x += 1
        else:
            x = 1
        p = py[i][0]
        ans.append((py[i][2], p, x))
    ans.sort(key=lambda x:x[0])
    for i in range(M):
        print('{0:06}{1:06}'.format(ans[i][1], ans[i][2]))
    # Print output here

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(M)]
    cities = sorted(cities, key=lambda x: x[1])
    prefectures = [0] * N
    for i in range(M):
        p, y = cities[i]
        prefectures[p-1] += 1
        cities[i].append(prefectures[p-1])
    cities = sorted(cities, key=lambda x: x[0])
    for i in range(M):
        p, y, n = cities[i]
        print("{:0>6}{:0>6}".format(p, n))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    PY = [[int(x) for x in input().split()] for _ in range(M)]
    PY = sorted(PY, key=lambda x: x[1])
    P = [0] * N
    for i in range(M):
        P[PY[i][0] - 1] += 1
        PY[i].append(P[PY[i][0] - 1])
    PY = sorted(PY, key=lambda x: x[2])
    for i in range(M):
        print(str(PY[i][0]).zfill(6) + str(PY[i][3]).zfill(6))
