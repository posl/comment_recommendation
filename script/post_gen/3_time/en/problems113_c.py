Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    P = [p-1 for p in P]
    YY = sorted([(y, i) for i, y in enumerate(Y)])
    PP = sorted([(p, i) for i, p in enumerate(P)])
    ans = [0] * M
    j = 0
    for i in range(M):
        while j < M and YY[j][0] <= Y[PP[i][1]]:
            ans[YY[j][1]] = str(PP[i][0]+1).zfill(6) + str(j+1).zfill(6)
            j += 1
    for i in range(M):
        print(ans[i])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    #print(P)
    #print(Y)

    # sort
    sorted_Y = sorted(Y)
    #print(sorted_Y)

    # sort by prefecture
    sorted_P = sorted(P)
    #print(sorted_P)

    # sorted index
    sorted_Y_index = sorted(range(len(Y)), key=lambda k: Y[k])
    #print(sorted_Y_index)

    # sorted Y by prefecture
    sorted_Y_by_P = []
    for i in range(N):
        sorted_Y_by_P.append([])
    for i in range(M):
        sorted_Y_by_P[P[sorted_Y_index[i]]-1].append(sorted_Y_index[i])
    #print(sorted_Y_by_P)

    for i in range(N):
        for j in range(len(sorted_Y_by_P[i])):
            sorted_Y_by_P[i][j] = str(sorted_Y_by_P[i][j]+1).zfill(6)
    #print(sorted_Y_by_P)

    # print answer
    for i in range(M):
        print(str(P[i]).zfill(6)+sorted_Y_by_P[P[i]-1].pop(0))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)

    P = [x-1 for x in P]
    P_Y = sorted(zip(P, Y))
    P_Y = [list(x) for x in P_Y]
    P_Y = sorted(P_Y, key=lambda x: x[1])

    ans = [0]*M
    for i in range(M):
        ans[P_Y[i][0]] += 1
        print("{:06}{:06}".format(P_Y[i][0]+1, ans[P_Y[i][0]]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    p = [0] * M
    y = [0] * M
    for i in range(M):
        p[i], y[i] = map(int, input().split())
    for i in range(M):
        print('{:06}{:06}'.format(p[i], y.index(y[i]) + 1))

=======
Suggestion 5

def main():
    #input
    N, M = map(int, input().split())
    P = [0] * M
    Y = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    #solve
    P = [P[i]-1 for i in range(M)]
    Y = [Y[i] for i in range(M)]
    pref = [[] for i in range(N)]
    for i in range(M):
        pref[P[i]].append(Y[i])
    for i in range(N):
        pref[i].sort()
    for i in range(M):
        j = pref[P[i]].index(Y[i])
        print('{:06d}'.format(P[i]+1) + '{:06d}'.format(j+1))
    #output

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cities = []
    for _ in range(M):
        P, Y = map(int, input().split())
        cities.append([P, Y])
    cities.sort(key=lambda x : x[1])
    p = 0
    y = 0
    for i in range(M):
        if cities[i][0] != p:
            p = cities[i][0]
            y = 1
        else:
            y += 1
        print("{0:06d}".format(p) + "{0:06d}".format(y))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(M)]
    city.sort(key=lambda x: (x[0], x[1]))
    ans = [0] * M
    for i in range(M):
        ans[i] = str(city[i][0]).zfill(6) + str(i+1).zfill(6)
    print('

'.join(ans))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(M)]
    # sort by Y_i
    cities.sort(key=lambda x: x[1])
    # sort by P_i
    cities.sort(key=lambda x: x[0])
    #print(cities)
    # count cities for each prefecture
    count = [0] * (N + 1)
    for city in cities:
        count[city[0]] += 1
    #print(count)
    # make ID numbers
    for city in cities:
        print("{:06}{:06}".format(city[0], count[city[0]]))
        count[city[0]] -= 1

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #P_i, Y_iを格納するリスト
    #リストの添字は0から始まるため、都道府県番号は-1して格納する
    #Y_iはその年に設立された都道府県の都市の数を格納する
    P_Y = [[0] * 2 for i in range(N)]
    #都道府県番号とその都道府県に所属する都市の数を格納する辞書
    #都道府県番号はそのまま格納する
    dict_P_Y = {}
    #都道府県番号とその都道府県に所属する都市のID番号を格納するリスト
    #都道府県番号は-1して格納する
    P_ID = [[] for i in range(N)]
    #都道府県番号とその都道府県に所属する都市のID番号を格納する辞書
    #都道府県番号はそのまま格納する
    dict_P_ID = {}
    #都道府県番号とその都道府県に所属する都市のID番号を格納するリスト
    #都道府県番号は-1して格納する
    P_ID = [[] for i in range(N)]
    #都道府県番号とその都道府県に所属する都市のID番号を格納する辞書
    #都道府県番号はそのまま格納する
    dict_P_ID = {}
    #都市のID番号を格納するリスト
    #リストの添字は0から始まるため、都市番号は-1して格納する
    ID = [0] * M
    #都市番号とその都市のID番号を格納する辞書
    #都市番
