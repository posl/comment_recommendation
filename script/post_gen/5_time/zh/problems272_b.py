Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        k, *x = map(int, input().split())
        for j in range(k):
            for l in range(j + 1, k):
                a[x[j] - 1][x[l] - 1] = 1
                a[x[l] - 1][x[j] - 1] = 1
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if a[i][j] == 0:
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    # 读入数据
    N, M = map(int, input().split())
    # 生成参加聚会的人的列表
    party = []
    for i in range(M):
        party.append(list(map(int, input().split()))[1:])
    # 生成关系矩阵
    relation = [[0] * N for i in range(N)]
    for i in range(M):
        for j in range(len(party[i])):
            for k in range(j + 1, len(party[i])):
                relation[party[i][j] - 1][party[i][k] - 1] = 1
                relation[party[i][k] - 1][party[i][j] - 1] = 1
    # 检查关系矩阵
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if relation[i][j] == 0:
                print("No")
                return
    print("Yes")

=======
Suggestion 3

def main():
    # 读取数据
    n, m = map(int, input().split())
    # 创建二维数组
    a = [[0] * n for i in range(n)]
    # 创建一个数组
    b = [0] * n
    # 读取数据
    for i in range(m):
        k, *x = map(int, input().split())
        # 读取数据，创建二维数组
        for j in range(k):
            a[x[j] - 1][x[(j + 1) % k] - 1] = 1
            a[x[(j + 1) % k] - 1][x[j] - 1] = 1
    # 遍历数组
    for i in range(n):
        for j in range(n):
            # 如果a[i][j]为1
            if a[i][j] == 1:
                # b[i]加1
                b[i] += 1
    # 遍历数组
    for i in range(n):
        # 如果b[i]不为0
        if b[i] != 0:
            # 遍历数组
            for j in range(n):
                # 如果a[i][j]为1
                if a[i][j] == 1:
                    # b[j]加1
                    b[j] += 1
    # 遍历数组
    for i in range(n):
        # 如果b[i]为0
        if b[i] == 0:
            # 输出No
            print("No")
            # 退出程序
            exit()
    # 输出Yes
    print("Yes")

=======
Suggestion 4

def solve():
    n, m = [int(i) for i in input().split()]
    people = []
    for i in range(m):
        people.append([int(i) for i in input().split()][1:])

    for i in range(n):
        for j in range(i + 1, n):
            for k in people:
                if i + 1 in k and j + 1 in k:
                    break
            else:
                print("No")
                return
    print("Yes")


solve()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    #print(N, M)
    x = []
    for i in range(M):
        x.append(list(map(int, input().split())))
        #print(x[i])

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                flag = 0
                for k in range(M):
                    if i+1 in x[k] and j+1 in x[k]:
                        flag = 1
                        break
                if flag == 0:
                    print("No")
                    return
    print("Yes")
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if not (i+1 in a[k] and j+1 in a[k]):
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("Yes")
        exit()
    print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        A.append(list(map(int, input().split())))
    flag = True
    for i in range(N):
        for j in range(i + 1, N):
            flag1 = False
            for k in range(M):
                if i + 1 in A[k] and j + 1 in A[k]:
                    flag1 = True
            if not flag1:
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 8

def get_input():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    return N, M, k, x

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = [[0]*n for _ in range(n)]
    for _ in range(m):
        k, *x = map(int, input().split())
        for i in range(k):
            for j in range(i+1,k):
                a[x[i]-1][x[j]-1] = 1
                a[x[j]-1][x[i]-1] = 1
    for i in range(n):
        if sum(a[i]) != n-1:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 10

def main():
    # 读取输入
    N, M = map(int, input().split())
    # 生成一个N*N的矩阵
    matrix = [[0 for i in range(N)] for j in range(N)]
    # 读取人员参加的聚会
    for i in range(M):
        # 读取每个人参加的聚会
        k, *x = map(int, input().split())
        # 生成一个人员参加的聚会的矩阵
        for j in range(k):
            for l in range(j + 1, k):
                matrix[x[j] - 1][x[l] - 1] += 1
                matrix[x[l] - 1][x[j] - 1] += 1
    # 判断是否每两个人都至少参加过一次同一个聚会
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] == 0:
                print('No')
                return
    print('Yes')
