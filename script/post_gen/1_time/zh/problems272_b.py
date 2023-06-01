Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = [[0]*n for i in range(n)]
    for i in range(m):
        data = list(map(int, input().split()))
        for j in range(1, data[0]+1):
            for k in range(j+1, data[0]+1):
                x[data[j]-1][data[k]-1] = 1
                x[data[k]-1][data[j]-1] = 1
    for i in range(n):
        for j in range(i+1, n):
            if x[i][j] == 0:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * m
    for i in range(m):
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(m):
                if i in a[k] and j in a[k]:
                    ans += 1
                    break
    if ans == n * (n - 1) // 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(N):
        for j in range(i + 1, N):
            flag = False
            for l in range(M):
                if i + 1 in x[l] and j + 1 in x[l]:
                    flag = True
            if not flag:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 4

def main():
    # 读取数据
    n, m = map(int, input().split())
    # print(n, m)
    # 读取第二行开始的m行数据，每行数据的第一个是参加聚会的人数，后面的是参加聚会的人的编号
    data = []
    for i in range(m):
        line = list(map(int, input().split()))
        # print(line)
        # 读取每行数据的第一个是参加聚会的人数，后面的是参加聚会的人的编号
        data.append(line[1:])
    # print(data)
    # 每两个人都至少参加过一次同一个聚会，则打印Yes；否则打印No。
    # 思路：两两比较
    for i in range(n):
        for j in range(n):
            if i != j:
                # print(i, j)
                # print(data[i], data[j])
                # 判断两个列表是否有交集
                if set(data[i]) & set(data[j]) == set():
                    print("No")
                    return
    print("Yes")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    x = []
    for i in range(M):
        x.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1, N):
            flag = False
            for k in range(M):
                if i+1 in x[k] and j+1 in x[k]:
                    flag = True
            if not flag:
                print("No")
                return
    print("Yes")

=======
Suggestion 6

def check_meeting(meeting, n):
    for i in range(n):
        for j in range(n):
            if i != j and meeting[i][j] == 0:
                return False
    return True

=======
Suggestion 7

def problem272_b():
    N,M = map(int,input().split())
    x = [[0 for i in range(N)] for j in range(M)]
    for i in range(M):
        x[i] = list(map(int,input().split()))
    for i in range(M):
        for j in range(M):
            if i != j:
                if len(set(x[i][1:]) & set(x[j][1:])) > 0:
                    continue
                else:
                    print('No')
                    return
    print('Yes')
    return


problem272_b()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for i in range(M)]
    ans = 'Yes'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if i+1 not in A[k] or j+1 not in A[k]:
                    ans = 'No'
                    break
    print(ans)

=======
Suggestion 9

def main():
    # 读取输入
    N, M = map(int, input().split())
    # 生成一个N*N的矩阵
    matrix = [[0] * N for i in range(N)]
    # 读取每一行的数据
    for i in range(M):
        # 读取每一行的数据
        row = list(map(int, input().split()))
        # 读取每一行的第一个数据，即人数
        k = row[0]
        # 读取每一行的后面数据，即每个人的编号
        # 两个人参加了同一个聚会，即两个人的编号在矩阵中对应的位置的值为1
        for j in range(1, k + 1):
            for l in range(j + 1, k + 1):
                matrix[row[j] - 1][row[l] - 1] = matrix[row[l] - 1][row[j] - 1] = 1
    # 判断矩阵中是否有0，如果有0，则说明有两个人没有参加同一个聚会
    # 如果没有0，则说明每两个人都参加了同一个聚会
    if 0 in matrix:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    #读入数据
    n,m=map(int,input().split())
    #print(n,m)
    #print(type(n))
    #print(type(m))
    #print(type(input()))
    #print(type(input().split()))
    #print(type(map(int,input().split())))
    #print(type(list(map(int,input().split()))))
    #print(list(map(int,input().split())))
    #print(type(list(map(int,input().split()))[0]))
    #print(type(list(map(int,input().split()))[1]))
    #print(type(list(map(int,input().split()))[2]))
    #print(type(list(map(int,input().split()))[3]))
    #print(type(list(map(int,input().split()))[4]))
    #print(type(list(map(int,input().split()))[5]))
    #print(type(list(map(int,input().split()))[6]))
    #print(type(list(map(int,input().split()))[7]))
    #print(type(list(map(int,input().split()))[8]))
    #print(type(list(map(int,input().split()))[9]))
    #print(type(list(map(int,input().split()))[10]))
    #print(type(list(map(int,input().split()))[11]))
    #print(type(list(map(int,input().split()))[12]))
    #print(type(list(map(int,input().split()))[13]))
    #print(type(list(map(int,input().split()))[14]))
    #print(type(list(map(int,input().split()))[15]))
    #print(type(list(map(int,input().split()))[16]))
    #print(type(list(map(int,input().split()))[17]))
    #print(type(list(map(int,input().split()))[18]))
    #print(type(list(map(int,input().split()))[19]))
    #print(type(list(map(int,input().split()))[20]))
    #print(type(list(map(int,input().split()))[21]))
    #print(type(list(map(int,input().split()))[22]))
    #print(type(list(map(int,input().split()))[23]))
    #print(type(list(map(int,input().split()))[24]))
    #print(type(list(map(int,input().split()))[25]))
    #print(type(list(map(int,input().split()))[26]))
    #print(type(list(map(int,input().split()))[27]))
    #print(type(list(map(int,input().split()))[28]))
    #print(type(list(map(int,input().split()))[
