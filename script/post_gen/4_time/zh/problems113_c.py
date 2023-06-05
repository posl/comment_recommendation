Synthesizing 10/10 solutions

=======
Suggestion 1

def id_generator(county, year, cities):
    id = ""
    for i in range(1, len(cities[county])+1):
        if cities[county][i] == year:
            id = str(county).zfill(6) + str(i).zfill(6)
            break
    return id

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: x[1])
    P_Y_dict = {}
    for i in range(M):
        P_Y_dict[P_Y[i][0]] = P_Y_dict.get(P_Y[i][0], 0) + 1
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6) + str(P_Y_dict[P_Y[i][0]]).zfill(6))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x: (x[0], x[1]))
    P = [0] * N
    Y = [0] * N
    for i in range(M):
        P[i] = P_Y[i][0]
        Y[i] = P_Y[i][1]
    cnt = [0] * N
    for i in range(M):
        cnt[P[i] - 1] += 1
    for i in range(M):
        print('{:06d}{:06d}'.format(P[i], cnt[P[i] - 1]))
        cnt[P[i] - 1] += 1

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(M):
        p, y = map(int, input().split())
        cities.append((i, p, y))

    cities.sort(key=lambda x: x[2])
    cities.sort(key=lambda x: x[1])

    ids = [0] * M
    for i in range(M):
        ids[cities[i][0]] = str(cities[i][1]).zfill(6) + str(i + 1).zfill(6)

    for i in range(M):
        print(ids[i])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    city = []
    for i in range(m):
        p, y = map(int, input().split())
        city.append([i, p, y])
    city.sort(key=lambda x: x[2])
    ans = []
    for i in range(m):
        ans.append([city[i][0], city[i][1], i + 1])
    ans.sort(key=lambda x: x[0])
    for i in range(m):
        print(str(ans[i][1]).zfill(6) + str(ans[i][2]).zfill(6))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    city = []
    for i in range(m):
        p,y = map(int,input().split())
        city.append([p,y,i])
    city.sort(key=lambda x:x[1])
    ans = []
    for i in range(m):
        p,y,idx = city[i]
        ans.append([p,str(i+1).zfill(6),idx])
    ans.sort(key=lambda x:x[2])
    for i in range(m):
        print(ans[i][0]+ans[i][1])

=======
Suggestion 7

def problems113_c():
    pass

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for i in range(M)]
    city.sort(key=lambda x: x[1])
    # print(city)
    ans = [0] * M
    cnt = [0] * N
    for i in range(M):
        p, y = city[i]
        cnt[p - 1] += 1
        ans[i] = [p, cnt[p - 1]]
    ans.sort(key=lambda x: x[1])
    # print(ans)
    for i in range(M):
        print(str(ans[i][0]).zfill(6) + str(ans[i][1]).zfill(6))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:(x[0],x[1]))
    p_y_dict = {}
    for i in range(m):
        if p_y[i][0] not in p_y_dict:
            p_y_dict[p_y[i][0]] = 1
        else:
            p_y_dict[p_y[i][0]] += 1
    for i in range(m):
        print(str(p_y[i][0]).zfill(6) + str(p_y_dict[p_y[i][0]]).zfill(6))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    PY = [list(map(int, input().split())) for _ in range(M)]

    PY.sort(key=lambda x: x[1])

    ans = [0] * M
    cnt = [1] * (N + 1)
    for i in range(M):
        p, y = PY[i]
        ans[i] = str(p).zfill(6) + str(cnt[p]).zfill(6)
        cnt[p] += 1

    for i in range(M):
        print(ans[i])
