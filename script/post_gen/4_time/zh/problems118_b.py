Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # read input
    line = input()
    line = line.split()
    N = int(line[0])
    M = int(line[1])
    #print(N,M)
    #print(type(N),type(M))
    #p

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    ans = 0
    for i in range(1, M+1):
        for j in range(N):
            if i not in A[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    cnt = [0] * M
    for i in range(N):
        for j in range(1, A[i][0] + 1):
            cnt[A[i][j] - 1] += 1
    ans = 0
    for i in range(M):
        if cnt[i] == N:
            ans += 1
    print(ans)

=======
Suggestion 4

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except EOFError:
            break
    return input_list

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    b = []
    for i in range(n):
        for j in range(1, len(a[i])):
            b.append(a[i][j])

    c = [0 for i in range(m)]
    for i in range(len(b)):
        c[b[i]-1] += 1

    ans = 0
    for i in range(len(c)):
        if c[i] == n:
            ans += 1

    print(ans)

=======
Suggestion 6

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]

    # 计算
    ans = 0
    for i in range(1, M+1):
        for j in range(N):
            if i in A[j]:
                continue
            break
        else:
            ans += 1

    # 打印结果
    print(ans)

=======
Suggestion 7

def get_input():
    N, M = input().split()
    N, M = int(N), int(M)
    K = []
    A = []
    for i in range(N):
        k, a = input().split()
        k = int(k)
        a = [int(i) for i in a]
        K.append(k)
        A.append(a)

    return N, M, K, A

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    K = []
    A = []
    for i in range(N):
        K.append(list(map(int,input().split())))
    for i in range(N):
        A.append(list(map(int,input().split())))
    #print(K)
    #print(A)
    #print(N,M)
    #print(len(K),len(A))
    #print(len(K[0]),len(A[0]))
    #print(K[0][0],A[0][0])
    #print(K[0][1],A[0][1])
    #print(K[0][2],A[0][2])
    #print(K[1][0],A[1][0])
    #print(K[1][1],A[1][1])
    #print(K[1][2],A[1][2])
    #print(K[1][3],A[1][3])
    #print(K[2][0],A[2][0])
    #print(K[2][1],A[2][1])
    #print(K[2][2],A[2][2])
    #print(K[2][3],A[2][3])
    #print(K[2][4],A[2][4])
    #print(K[3][0],A[3][0])
    #print(K[3][1],A[3][1])
    #print(K[3][2],A[3][2])
    #print(K[3][3],A[3][3])
    #print(K[3][4],A[3][4])
    #print(K[4][0],A[4][0])
    #print(K[4][1],A[4][1])
    #print(K[4][2],A[4][2])
    #print(K[4][3],A[4][3])
    #print(K[4][4],A[4][4])
    #print(K[4][5],A[4][5])
    #print(K[4][6],A[4][6])
    #print(K[4][7],A[4][7])
    #print(K[4][8],A[4][8])
    #print(K[4][9],A[4][9])
    #print

=======
Suggestion 9

def getNumOfLikeFood():
    N, M = map(int, input().split())
    num = 0
    food = [0] * M
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(1, temp[0] + 1):
            food[temp[j] - 1] += 1
    for i in range(M):
        if food[i] == N:
            num += 1
    print(num)

getNumOfLikeFood()

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(N):
        K.append(list(map(int, input().split())))
        A.append(list(map(int, input().split())))
    #print(N, M, K, A)
    #print(K[0][0])
    #print(A[0][0])
    count = 0
    for i in range(1, M+1):
        for j in range(N):
            if i in A[j]:
                #print(i)
                if j == N-1:
                    count += 1
                    #print(count)
            else:
                break
    print(count)
