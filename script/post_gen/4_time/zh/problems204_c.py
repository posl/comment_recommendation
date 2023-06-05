Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N * (N - 1) // 2 - M)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    count = 0
    for i in range(m):
        if a[i] != b[i]:
            count += 1
    count = count * 2 + 1
    print(count)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    for i in range(m):
        a[i] -= 1
        b[i] -= 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                cnt = 0
                for k in range(m):
                    if a[k] == i and b[k] == j:
                        cnt += 1
                ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 4

def cal(N,M,city):
    result=0
    for i in range(N):
        for j in range(N):
            if i==j:
                result+=1
                continue
            flag=0
            for k in range(M):
                if city[k][0]==i+1 and city[k][1]==j+1:
                    flag=1
                    break
            if flag==0:
                result+=1
    return result

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans += a.count(i+1) * b.count(j+1)
    print(ans)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    #print(N,M,A,B)
    #print(A)
    #print(B)
    #print(A[0])
    #print(B[0])
    #print(A[1])
    #print(B[1])
    #print(A[2])
    #print(B[2])
    #print(A[3])
    #print(B[3])
    #print(A[4])
    #print(B[4])
    #print(A[5])
    #print(B[5])
    #print(A[6])
    #print(B[6])
    #print(A[7])
    #print(B[7])
    #print(A[8])
    #print(B[8])
    #print(A[9])
    #print(B[9])
    #print(A[10])
    #print(B[10])
    #print(A[11])
    #print(B[11])
    #print(A[12])
    #print(B[12])
    #print(A[13])
    #print(B[13])
    #print(A[14])
    #print(B[14])
    #print(A[15])
    #print(B[15])
    #print(A[16])
    #print(B[16])
    #print(A[17])
    #print(B[17])
    #print(A[18])
    #print(B[18])
    #print(A[19])
    #print(B[19])
    #print(A[20])
    #print(B[20])
    #print(A[21])
    #print(B[21])
    #print(A[22])
    #print(B[22])
    #print(A[23])
    #print(B[23])
    #print(A[24])
    #print(B[24])
    #print(A[25])
    #print(B[25])
    #print(A[26])
    #print(B[26])
    #print(A[27])
    #print(B[27])
    #print(A[28])
    #print(B[28])
    #print(A[29])
    #print(B[29])
    #print(A[30])
    #print(B

=======
Suggestion 7

def main():
    # 读入数据
    n, m = map(int, input().split())
    # 读入道路
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))
    # print(road)
    # 建立邻接矩阵
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in road:
        matrix[i[0]-1][i[1]-1] = 1
    # print(matrix)
    # 遍历邻接矩阵
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1:
                        if matrix[k][i] == 1:
                            count += 1
    print(count)

=======
Suggestion 8

def calc(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return calc(a, b - 1) + calc(a, b - 2) + calc(a, b - 3)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    print(N,M)
    print("Hello World!")
    return 0
