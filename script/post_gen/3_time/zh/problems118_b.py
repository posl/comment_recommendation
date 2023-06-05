Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(N):
        K.append(int(input().split()[0]))
        A.append(list(map(int, input().split())))

    # print(K)
    # print(A)

    count = 0
    for i in range(1, M+1):
        for j in range(N):
            if i in A[j]:
                if j == N-1:
                    count += 1
            else:
                break

    print(count)

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
    #print(N, M)
    #print(K)
    #print(A)

    #print(len(A))
    #print(len(A[0]))
    #print(A[0][0])

    #print(len(A[1]))
    #print(A[1][1])
    #print(A[1][2])

    #print(len(A[2]))
    #print(A[2][0])
    #print(A[2][1])

    #print(len(A[3]))
    #print(A[3][0])
    #print(A[3][1])
    #print(A[3][2])

    #print(len(A[4]))
    #print(A[4][0])
    #print(A[4][1])
    #print(A[4][2])
    #print(A[4][3])

    #print(len(A[5]))
    #print(A[5][0])
    #print(A[5][1])
    #print(A[5][2])
    #print(A[5][3])
    #print(A[5][4])

    #print(len(A[6]))
    #print(A[6][0])
    #print(A[6][1])
    #print(A[6][2])
    #print(A[6][3])
    #print(A[6][4])
    #print(A[6][5])

    #print(len(A[7]))
    #print(A[7][0])
    #print(A[7][1])
    #print(A[7][2])
    #print(A[7][3])
    #print(A[7][4])
    #print(A[7][5])
    #print(A[7][6])

    #print(len(A[8]))
    #print(A[8][0])
    #print(A[8][1])
    #print(A[8][2])
    #print(A[8][3])
    #print(A[8][4])
    #print(A[8][5])
    #print(A[8][6])
    #print(A[8][7])

    #print(len(A[9]))
    #print

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [[0] for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    #print(a)
    ans = 0
    for i in range(1, m + 1):
        for j in range(n):
            if i in a[j][1:]:
                if j == n - 1:
                    ans += 1
            else:
                break
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    like = [0] * M
    for i in range(N):
        for j in range(A[i][0]):
            like[A[i][j+1]-1] += 1
    print(like.count(N))

=======
Suggestion 5

def get_input():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    return N, M, A

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    k = [0]*n
    a = [0]*n
    for i in range(n):
        k[i],*a[i] = map(int,input().split())
    count = 0
    for i in range(1,m+1):
        flag = True
        for j in range(n):
            if i in a[j]:
                pass
            else:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = [[0 for i in range(0,M)] for j in range(0,N)]
    for i in range(0,N):
        A[i] = list(map(int,input().split()))
    #print(A)
    food = [0 for i in range(0,M)]
    for i in range(0,N):
        for j in range(1,A[i][0]+1):
            food[A[i][j]-1] += 1
    #print(food)
    count = 0
    for i in range(0,M):
        if food[i] == N:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = []
    for i in range(N):
        A.append(list(map(int,input().split()))[1:])
    like = set(A[0])
    for i in range(1,N):
        like = like & set(A[i])
    print(len(like))
main()

=======
Suggestion 9

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]

    # 枚举所有食物
    ans = 0
    for i in range(1, M + 1):
        # 判断是否所有人都喜欢食物 i
        for a in A:
            if i not in a:
                break
        else:
            ans += 1

    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(n):
        k.append(list(map(int, input().split())))
    for i in range(n):
        a.append(k[i][1:])
    b = []
    for i in range(n):
        for j in range(k[i][0]):
            b.append(a[i][j])
    c = sorted(b)
    d = []
    for i in range(len(c)):
        if c[i] == c[i-1]:
            d.append(c[i])
    e = set(d)
    f = list(e)
    print(len(f))
