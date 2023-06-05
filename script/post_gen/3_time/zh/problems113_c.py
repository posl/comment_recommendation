Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for i in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y2 = [p_y[i]+[i] for i in range(m)]
    p_y2.sort(key=lambda x:x[2])
    ans = []
    for i in range(m):
        ans.append([p_y2[i][0],p_y2[i][2]+1])
    ans.sort(key=lambda x:x[1])
    for i in range(m):
        print(str(ans[i][0]).zfill(6)+str(ans[i][1]).zfill(6))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    lst = []
    for i in range(M):
        lst.append(list(map(int, input().split())))
    lst = sorted(lst, key=lambda x: x[1])
    dic = {}
    for i in range(M):
        if lst[i][0] not in dic:
            dic[lst[i][0]] = 1
        else:
            dic[lst[i][0]] += 1
        print(str(lst[i][0]).zfill(6) + str(dic[lst[i][0]]).zfill(6))

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    #print(N,M)
    input_list = []
    for i in range(M):
        input_list.append(list(map(int,input().split())))
    #print(input_list)
    input_list = sorted(input_list,key=lambda x:x[1])
    #print(input_list)
    input_dict = {}
    for i in range(M):
        if input_list[i][0] not in input_dict:
            input_dict[input_list[i][0]] = 1
        else:
            input_dict[input_list[i][0]] += 1
    #print(input_dict)
    input_dict2 = {}
    for i in range(M):
        if input_list[i][0] not in input_dict2:
            input_dict2[input_list[i][0]] = 1
        else:
            input_dict2[input_list[i][0]] += 1
        input_list[i].append(input_dict2[input_list[i][0]])
    #print(input_list)
    input_list = sorted(input_list,key=lambda x:x[0])
    #print(input_list)
    for i in range(M):
        print(str(input_list[i][0]).zfill(6)+str(input_list[i][3]).zfill(6))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        P, Y = map(int, input().split())
        city.append([P, Y, i])
    city.sort(key=lambda x: x[1])
    count = [0] * (N + 1)
    ans = []
    for i in range(M):
        count[city[i][0]] += 1
        ans.append([city[i][0], count[city[i][0]], city[i][2]])
    ans.sort(key=lambda x: x[2])
    for i in range(M):
        print(str(ans[i][0]).zfill(6) + str(ans[i][1]).zfill(6))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        P, Y = map(int, input().split())
        city.append([i, P, Y])
    city.sort(key=lambda x: x[2])
    city.sort(key=lambda x: x[1])
    #print(city)
    #for i in range(M):
    #    print(city[i][0], city[i][1], city[i][2])
    ans = [0] * M
    count = [0] * (N + 1)
    for i in range(M):
        count[city[i][1]] += 1
        ans[city[i][0]] = str(city[i][1]).zfill(6) + str(count[city[i][1]]).zfill(6)
    for i in range(M):
        print(ans[i])

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    P_Y = [list(map(int,input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x:x[1])
    #print(P_Y)
    city = [0]*N
    for i in range(M):
        city[P_Y[i][0]-1] += 1
    #print(city)
    for i in range(M):
        print(str(P_Y[i][0]).zfill(6)+str(city[P_Y[i][0]-1]).zfill(6))

=======
Suggestion 7

def problem113_c():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y_dict = {}
    for p, y in p_y:
        if p not in p_y_dict:
            p_y_dict[p] = 1
        else:
            p_y_dict[p] += 1
    ans = {}
    for p, y in p_y:
        ans[y] = str(p).zfill(6) + str(p_y_dict[p]).zfill(6)
        p_y_dict[p] -= 1
    for y in p_y:
        print(ans[y[1]])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    for i in range(M):
        P[i] = str(P[i]).zfill(6)
        Y[i] = str(Y[i]).zfill(6)
    for i in range(M):
        print(P[i]+Y[i])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    city = []
    for i in range(M):
        P, Y = map(int, input().split())
        city.append([P, Y, i])
    city.sort(key=lambda x: x[1])
    ans = [None] * M
    for i in range(M):
        ans[city[i][2]] = '{:06}{:06}'.format(city[i][0], i + 1)
    for i in range(M):
        print(ans[i])

=======
Suggestion 10

def problems113_c():
    pass
