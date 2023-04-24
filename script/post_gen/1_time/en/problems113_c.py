Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    p_y = sorted(zip(p, y, range(m)))
    r = [0] * m
    c = [0] * (n + 1)
    for i in range(m):
        c[p_y[i][0]] += 1
        r[p_y[i][2]] = '{:06}{:06}'.format(p_y[i][0], c[p_y[i][0]])
    print('

'.join(r))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    P = [0]*M
    Y = [0]*M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    # sort by P, Y
    P_sorted = sorted(range(M), key=lambda k: P[k])
    P_sorted2 = sorted(range(M), key=lambda k: Y[k])
    #print(P_sorted)
    #print(P_sorted2)
    #print(P)
    #print(Y)
    #print(P[P_sorted[0]])
    #print(Y[P_sorted2[0]])
    #print(P[P_sorted[1]])
    #print(Y[P_sorted2[1]])
    #print(P[P_sorted[2]])
    #print(Y[P_sorted2[2]])
    #print(P[P_sorted[3]])
    #print(Y[P_sorted2[3]])
    #print(P[P_sorted[4]])
    #print(Y[P_sorted2[4]])
    #print(P[P_sorted[5]])
    #print(Y[P_sorted2[5]])
    #print(P[P_sorted[6]])
    #print(Y[P_sorted2[6]])
    #print(P[P_sorted[7]])
    #print(Y[P_sorted2[7]])
    #print(P[P_sorted[8]])
    #print(Y[P_sorted2[8]])
    #print(P[P_sorted[9]])
    #print(Y[P_sorted2[9]])
    #print(P[P_sorted[10]])
    #print(Y[P_sorted2[10]])
    #print(P[P_sorted[11]])
    #print(Y[P_sorted2[11]])
    #print(P[P_sorted[12]])
    #print(Y[P_sorted2[12]])
    #print(P[P_sorted[13]])
    #print(Y[P_sorted2[13]])
    #print(P[P_sorted[14]])
    #print(Y[P_sorted2[14]])
    #print(P[P_sorted[15]])
    #print(Y[P_sorted2[15]])
    #print(P[P_sorted[16]])
    #print(Y[P_sorted2[16]])
    #print(P[P_sorted[17]])
    #print(Y[P_sorted2[17]])
    #print(P[P_sorted[18]])
    #print(Y[P_sorted2[18]])
    #print(P[P_sorted[19]])
    #print(Y[P_sorted2[19]])
    #print(P[P_sorted

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        P_i, Y_i = map(int, input().split())
        P.append(P_i)
        Y.append(Y_i)
    #print(P)
    #print(Y)
    P_sorted = sorted(P)
    #print(P_sorted)
    P_sorted = sorted(P)
    #print(P_sorted)
    P_sorted_index = []
    for i in range(M):
        P_sorted_index.append(P_sorted.index(P[i]))
    #print(P_sorted_index)
    P_sorted_index_sorted = sorted(P_sorted_index)
    #print(P_sorted_index_sorted)
    P_sorted_index_sorted_index = []
    for i in range(M):
        P_sorted_index_sorted_index.append(P_sorted_index_sorted.index(P_sorted_index[i]))
    #print(P_sorted_index_sorted_index)
    for i in range(M):
        print("{0:06d}".format(P[i]) + "{0:06d}".format(P_sorted_index_sorted_index[i]+1))
    return

=======
Suggestion 4

def main():
    #input
    N, M = map(int, input().split())
    P, Y = [], []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)

    #compute
    ans = [0]*M
    for i in range(N):
        p = i+1
        dic = {}
        for j in range(M):
            if P[j] == p:
                y = Y[j]
                if y in dic:
                    dic[y] += 1
                else:
                    dic[y] = 1
        for j in range(M):
            if P[j] == p:
                y = Y[j]
                ans[j] = str(p).zfill(6) + str(dic[y]).zfill(6)
                dic[y] -= 1

    #output
    for i in range(M):
        print(ans[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        p, y = map(int, input().split())
        city.append([i, p, y])
    city.sort(key=lambda x: x[1])
    city.sort(key=lambda x: x[2])
    pref = [0 for i in range(N+1)]
    for i in range(M):
        pref[city[i][1]] += 1
        city[i].append(pref[city[i][1]])
    city.sort(key=lambda x: x[0])
    for i in range(M):
        print("{0:06d}{1:06d}".format(city[i][1], city[i][3]))

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    P = [0]*M
    Y = [0]*M
    for i in range(M):
        P[i], Y[i] = map(int,input().split())
    P = [p-1 for p in P]
    #print(P)
    #print(Y)
    #print(N,M)
    #print(P)
    #print(Y)
    Y_sorted = sorted(Y)
    #print(Y_sorted)
    P_sorted = sorted(P)
    #print(P_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted)
    #print(P_sorted)
    #print(Y_sorted)
    P_sorted = sorted(P_sorted)
    #print(P_sorted)
    Y_sorted = sorted(Y_sorted)
    #print(Y_sorted

=======
Suggestion 7

def main():
    N, M = [int(x) for x in input().split()]
    city = [tuple(int(x) for x in input().split()) for _ in range(M)]
    city.sort(key=lambda x: x[1])
    pref = [[] for _ in range(N)]
    for i in range(M):
        pref[city[i][0]-1].append(i)
    ans = [None] * M
    for i in range(N):
        for j in range(len(pref[i])):
            ans[pref[i][j]] = str(i+1).zfill(6) + str(j+1).zfill(6)
    print('

'.join(ans))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    # 1-indexed
    city = [list(map(int, input().split())) + [i] for i in range(m)]
    city.sort(key=lambda x: x[1])
    ans = [0] * m
    for i in range(m):
        ans[city[i][2]] = f'{city[i][0]:0>6}{i + 1:0>6}'
    print('

'.join(ans))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    # city list
    city = [list(map(int, input().split())) for _ in range(m)]
    # city list by prefecture
    city_by_pref = [[] for _ in range(n)]
    for i, c in enumerate(city):
        city_by_pref[c[0] - 1].append([i, c[1]])
    # sort city list by prefecture
    for p in city_by_pref:
        p.sort(key=lambda x: x[1])
    # output
    for p in city_by_pref:
        for i, c in enumerate(p):
            print("{:0=6}{:0=6}".format(c[1], i + 1))
