Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    P = [p - 1 for p in P]
    P_index = [0] * N
    P_list = [[] for _ in range(N)]
    for i, p in enumerate(P):
        P_list[p].append((Y[i], i))
    for i in range(N):
        P_list[i].sort()
    for i in range(N):
        for j in range(len(P_list[i])):
            P_list[i][j] = (P_list[i][j][0], i, j + 1)
    P_list.sort(key=lambda x: x[0][1])
    P_list.sort(key=lambda x: x[0][0])
    ans = [0] * M
    for i in range(N):
        for j in range(len(P_list[i])):
            ans[P_list[i][j][1]] = str(P_list[i][j][1] + 1).zfill(6) + str(P_list[i][j][2]).zfill(6)
    print('

'.join(ans))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    P = [x-1 for x in P]
    #P[i

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    P = np.array(P)
    Y = np.array(Y)
    P_sort = np.argsort(P)
    P = P[P_sort]
    Y = Y[P_sort]
    P_diff = np.diff(P)
    P_diff = np.append(P_diff, 1)
    P_diff = np.cumsum(P_diff)
    P_diff = np.append(0, P_diff)
    P_diff = P_diff[0:M]
    P_diff = P_diff.astype(np.str)
    P_diff = np.char.zfill(P_diff, 6)
    Y = Y.astype(np.str)
    Y = np.char.zfill(Y, 6)
    ans = P_diff + Y
    ans = ans.astype(np.int)
    ans_sort = np.argsort(ans)
    ans = ans[ans_sort]
    ans = ans.astype(np.str)
    ans = np.char.zfill(ans, 12)
    for i in range(M):
        print(ans[i])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    ans = solve(N, M, P, Y)
    for i in range(M):
        print(ans[i])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p = [0] * m
    y = [0] * m
    for i in range(m):
        p[i], y[i] = map(int, input().split())
    p = [p[i] - 1 for i in range(m)]
    y = [y[i] - 1 for i in range(m)]
    d = dict()
    for i in range(m):
        if p[i] in d:
            d[p[i]].append(y[i])
        else:
            d[p[i]] = [y[i]]
    for k in d:
        d[k].sort()
    for i in range(m):
        print('{:06d}{:06d}'.format(p[i] + 1, d[p[i]].index(y[i]) + 1))

=======
Suggestion 6

def main():
    N, M = input().split()
    N = int(N)
    M = int(M)
    P = []
    Y = []
    for i in range(M):
        p, y = input().split()
        P.append(int(p))
        Y.append(int(y))
    P = np.array(P)
    Y = np.array(Y)
    P = P - 1
    Y = Y - 1
    Y = Y.astype(str)
    Y = Y.tolist()
    Y = [i.zfill(6) for i in Y]
    P = P.astype(str)
    P = P.tolist()
    P = [i.zfill(6) for i in P]
    P = np.array(P)
    Y = np.array(Y)
    P = P.reshape(M,1)
    Y = Y.reshape(M,1)
    data = np.hstack((P,Y))
    data = data.astype(str)
    data = data.tolist()
    data = ["".join(i) for i in data]
    data = np.array(data)
    data = data.reshape(M,1)
    data = np.sort(data)
    data = data.reshape(M,)
    data = data.tolist()
    data = [i.zfill(12) for i in data]
    for i in range(M):
        print(data[i])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(M)]
    city.sort(key=lambda x: x[1])
    cnt = [0] * (N+1)
    for i in range(M):
        cnt[city[i][0]] += 1
        city[i].append(cnt[city[i][0]])
    city.sort(key=lambda x: x[0])
    for i in range(M):
        print(str(city[i][0]).zfill(6) + str(city[i][2]).zfill(6))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        city.append(list(map(int, input().split())))
    city.sort(key=lambda x: x[1])
    ans = []
    for i in range(M):
        ans.append(str(city[i][0]).zfill(6) + str(i + 1).zfill(6))

    ans.sort(key=lambda x: int(x[:6]))
    for i in range(M):
        print(ans[i])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(M)]
    cities.sort(key=lambda x: x[1])
    
    ans = [0] * M
    pref = [0] * (N + 1)
    for i, (p, y) in enumerate(cities):
        pref[p] += 1
        ans[i] = '{:06}{:06}'.format(p, pref[p])
    
    print(*ans, sep='

')

main()
