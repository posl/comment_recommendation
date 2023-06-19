Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # N, M = list(map(int, input().split()))
    # A = []
    # for i in range(N):
    #     A.append(list(map(int, input().split()))[1:])
    # print(len(set.intersection(*map(set, A))))
    N, M = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    print(len(set.intersection(*map(set, A))))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    food = [0] * M
    for i in range(N):
        for j in range(1, A[i][0] + 1):
            food[A[i][j] - 1] += 1
    print(food.count(N))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    #print(N, M, A)

    # 与えられたN人のうち、全員が好きな食べ物の数を数える
    # 食べ物の数を数える
    # 食べ物を数える
    #print(A)
    like = [0] * M
    for i in range(N):
        for j in range(len(A[i])):
            like[A[i][j]-1] += 1
    #print(like)
    cnt = 0
    for i in range(M):
        if like[i] == N:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    k = [0] * n
    a = [0] * n
    for i in range(n):
        k[i], *a[i] = map(int, input().split())
    #print(k)
    #print(a)
    like = [0] * m
    for i in range(n):
        for j in range(k[i]):
            like[a[i][j] - 1] += 1
    #print(like)
    count = 0
    for i in range(m):
        if like[i] == n:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    k = []
    for i in range(n):
        k.append(list(map(int,input().split())))
    result = 0
    for i in range(1,m+1):
        flag = True
        for j in range(n):
            if i not in k[j][1:]:
                flag = False
                break
        if flag:
            result += 1
    print(result)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(n):
        k.append(list(map(int, input().split())))
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(m):
        flag = True
        for j in range(n):
            if i + 1 not in a[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    #print(a)
    #print(n,m)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[1][3])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[2][3])
    #print(a[2][4])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[3][2])
    #print(a[3][3])
    #print(a[3][4])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[4][2])
    #print(a[4][3])
    #print(a[4][4])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[5][2])
    #print(a[5][3])
    #print(a[5][4])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[6][2])
    #print(a[6][3])
    #print(a[6][4])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[7][2])
    #print(a[7][3])
    #print(a[7][4])
    #print(a[8][0])
    #print(a[8][1])
    #print(a[8][2])
    #print(a[8][3])
    #print(a[8][4])
    #print(a[9][0])
    #print(a[9][1])
    #print(a[9][2])
    #print(a[9][3])
    #print(a[9][4])
    #print(a[10][0])
    #print(a[10][1])
    #print(a[10][2])
    #print(a[10

=======
Suggestion 8

def main():
    n,m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    b = [0] * m
    for i in range(n):
        for j in range(1, a[i][0]+1):
            b[a[i][j]-1] += 1
    print(b.count(n))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()[1:])))
    from itertools import combinations
    ans = 0
    for i in combinations(range(1, m+1), 1):
        for j in a:
            if not i[0] in j:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    # 读取数据
    n, m = map(int, input().split())
    # print(n, m)
    # print(type(n))
    # print(type(m))
    # print(type(input()))
    # print(type(input().split()))
    # print(type(map(int, input().split())))
    # print(type(list(map(int, input().split()))))
    # print(type(list(map(int, input().split()))[0]))
    # print(type(list(map(int, input().split()))[1]))
    # print(type(list(map(int, input().split()))[2]))
    # print(type(list(map(int, input().split()))[3]))
    # print(type(list(map(int, input().split()))[4]))
    # print(type(list(map(int, input().split()))[5]))
    # print(type(list(map(int, input().split()))[6]))
    # print(type(list(map(int, input().split()))[7]))
    # print(type(list(map(int, input().split()))[8]))
    # print(type(list(map(int, input().split()))[9]))
    # print(type(list(map(int, input().split()))[10]))
    # print(type(list(map(int, input().split()))[11]))
    # print(type(list(map(int, input().split()))[12]))
    # print(type(list(map(int, input().split()))[13]))
    # print(type(list(map(int, input().split()))[14]))
    # print(type(list(map(int, input().split()))[15]))
    # print(type(list(map(int, input().split()))[16]))
    # print(type(list(map(int, input().split()))[17]))
    # print(type(list(map(int, input().split()))[18]))
    # print(type(list(map(int, input().split()))[19]))
    # print(type(list(map(int, input().split()))[20]))
    # print(type(list(map(int, input().split()))[21]))
    # print(type(list(map(int, input().split()))[22]))
    # print(type(list(map(int, input().split()))[23]))
    # print(type(list(map(int, input().split()))[24]))
    # print(type(list(map(int, input().split()))[25]))
    # print(type(list(map(int, input().split()))[26]))
    # print(type(list(map(int, input().split()))[27]))
    #
