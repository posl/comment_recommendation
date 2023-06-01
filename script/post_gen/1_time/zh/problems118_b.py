Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, m, a):
    ans = 0
    for i in range(1, m + 1):
        flag = True
        for j in range(n):
            if i not in a[j]:
                flag = False
        if flag:
            ans += 1
    return ans

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(N):
        k, *a = map(int, input().split())
        K.append(k)
        A.append(a)
    # print(K, A)
    # print(A[0][0])
    # print(A[1][0])
    # print(A[2][0])
    # print(A[3][0])
    # print(A[4][0])
    # print(A[0][1])
    # print(A[1][1])
    # print(A[2][1])
    # print(A[3][1])
    # print(A[4][1])
    # print(A[0][2])
    # print(A[1][2])
    # print(A[2][2])
    # print(A[3][2])
    # print(A[4][2])
    # print(A[0][3])
    # print(A[1][3])
    # print(A[2][3])
    # print(A[3][3])
    # print(A[4][3])
    # print(A[0][4])
    # print(A[1][4])
    # print(A[2][4])
    # print(A[3][4])
    # print(A[4][4])
    # print(A[0][5])
    # print(A[1][5])
    # print(A[2][5])
    # print(A[3][5])
    # print(A[4][5])
    # print(A[0][6])
    # print(A[1][6])
    # print(A[2][6])
    # print(A[3][6])
    # print(A[4][6])
    # print(A[0][7])
    # print(A[1][7])
    # print(A[2][7])
    # print(A[3][7])
    # print(A[4][7])
    # print(A[0][8])
    # print(A[1][8])
    # print(A[2][8])
    # print(A[3][8])
    # print(A[4][8])
    # print(A[0][9])
    # print(A[1][9])
    # print(A[2][9])
    # print(A[3][9])

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    #print(A)
    #print(N,M)
    #print(A[0][0])
    #print(A[0][1])

    #print(A[0][0])
    #print(A[0][1])
    #print(A[0][2])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[2][0])
    #print(A[2][1])

    #print(A[0][0])
    #print(A[0][1])
    #print(A[0][2])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[3][0])
    #print(A[3][1])
    #print(A[4][0])
    #print(A[4][1])

    #print(A[0][0])
    #print(A[0][1])
    #print(A[0][2])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[3][0])
    #print(A[3][1])
    #print(A[4][0])
    #print(A[4][1])
    #print(A[5][0])
    #print(A[5][1])
    #print(A[6][0])
    #print(A[6][1])
    #print(A[7][0])
    #print(A[7][1])
    #print(A[8][0])
    #print(A[8][1])
    #print(A[9][0])
    #print(A[9][1])
    #print(A[10][0])
    #print(A[10][1])
    #print(A[11][0])
    #print(A[11][1])
    #print(A[12][0])
    #print(A[12][1])
    #print(A[13

=======
Suggestion 4

def main():
    # 输入
    n, m = map(int, input().split())
    # 初始化
    food = [0] * m
    # 循环输入
    for i in range(n):
        # 输入
        _, *a = map(int, input().split())
        # 循环统计
        for j in a:
            food[j - 1] += 1
    # 输出
    print(food.count(n))

=======
Suggestion 5

def main():
    # 读取输入
    n,m = map(int,input().split())
    a = [[int(i) for i in input().split()] for j in range(n)]
    # print(a)
    # 初始化
    like = [0 for i in range(m)]
    # print(like)
    # 统计喜欢的次数
    for i in range(n):
        for j in range(a[i][0]):
            like[a[i][j+1]-1] += 1
    # print(like)
    # 统计喜欢的食物数
    count = like.count(n)
    # print(count)
    # 输出
    print(count)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(N):
        k, *a = map(int, input().split())
        K.append(k)
        A.append(a)
    count = 0
    for i in range(1, M + 1):
        for j in range(N):
            if i in A[j]:
                count += 1
        if count == N:
            break
        count = 0
    print(count)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    k = []
    a = []
    for i in range(n):
        k.append(list(map(int,input().split())))
        a.append(list(map(int,input().split())))

    food = [0]*m
    for i in range(n):
        for j in range(k[i][0]):
            food[a[i][j]-1] += 1

    count = 0
    for i in range(m):
        if food[i] == n:
            count += 1

    print(count)

=======
Suggestion 8

def main():
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()
    line6 = input()
    line7 = input()
    line8 = input()
    line9 = input()
    line10 = input()
    line11 = input()
    line12 = input()
    line13 = input()
    line14 = input()
    line15 = input()
    line16 = input()
    line17 = input()
    line18 = input()
    line19 = input()
    line20 = input()
    line21 = input()
    line22 = input()
    line23 = input()
    line24 = input()
    line25 = input()
    line26 = input()
    line27 = input()
    line28 = input()
    line29 = input()
    line30 = input()
    line31 = input()
    line32 = input()
    line33 = input()
    line34 = input()
    line35 = input()
    line36 = input()
    line37 = input()
    line38 = input()
    line39 = input()
    line40 = input()
    line41 = input()
    line42 = input()
    line43 = input()
    line44 = input()
    line45 = input()
    line46 = input()
    line47 = input()
    line48 = input()
    line49 = input()
    line50 = input()
    line51 = input()
    line52 = input()
    line53 = input()
    line54 = input()
    line55 = input()
    line56 = input()
    line57 = input()
    line58 = input()
    line59 = input()
    line60 = input()
    line61 = input()
    line62 = input()
    line63 = input()
    line64 = input()
    line65 = input()
    line66 = input()
    line67 = input()
    line68 = input()
    line69 = input()
    line70 = input()
    line71 = input()
    line72 = input()
    line73 = input()
    line74 = input()
    line75 = input()
    line76 = input()
    line77 = input()
    line78 = input()
    line79 = input()
    line80 = input()
    line81 = input()
    line82 = input()
    line83 = input()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, m + 1):
        for j in range(n):
            if not i in a[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    k = []
    a = []
    for i in range(n):
        k.append(list(map(int,input().split())))
        a.append(list(map(int,input().split())))
    result = 0
    for i in range(1,m+1):
        flag = True
        for j in range(n):
            if i not in a[j]:
                flag = False
        if flag:
            result += 1
    print(result)

=======
Suggestion 8

def main():
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()
    line6 = input()
    line7 = input()
    line8 = input()
    line9 = input()
    line10 = input()
    line11 = input()
    line12 = input()
    line13 = input()
    line14 = input()
    line15 = input()
    line16 = input()
    line17 = input()
    line18 = input()
    line19 = input()
    line20 = input()
    line21 = input()
    line22 = input()
    line23 = input()
    line24 = input()
    line25 = input()
    line26 = input()
    line27 = input()
    line28 = input()
    line29 = input()
    line30 = input()
    line31 = input()
    line32 = input()
    line33 = input()
    line34 = input()
    line35 = input()
    line36 = input()
    line37 = input()
    line38 = input()
    line39 = input()
    line40 = input()
    line41 = input()
    line42 = input()
    line43 = input()
    line44 = input()
    line45 = input()
    line46 = input()
    line47 = input()
    line48 = input()
    line49 = input()
    line50 = input()
    line51 = input()
    line52 = input()
    line53 = input()
    line54 = input()
    line55 = input()
    line56 = input()
    line57 = input()
    line58 = input()
    line59 = input()
    line60 = input()
    line61 = input()
    line62 = input()
    line63 = input()
    line64 = input()
    line65 = input()
    line66 = input()
    line67 = input()
    line68 = input()
    line69 = input()
    line70 = input()
    line71 = input()
    line72 = input()
    line73 = input()
    line74 = input()
    line75 = input()
    line76 = input()
    line77 = input()
    line78 = input()
    line79 = input()
    line80 = input()
    line81 = input()
    line82 = input()
    line83 = input()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, m + 1):
        for j in range(n):
            if not i in a[j]:
                break
        else:
            ans += 1
    print(ans)
