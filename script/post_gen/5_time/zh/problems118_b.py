Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取数据
    n, m = map(int, input().split())
    like = [set(map(int, input().split()[1:])) for _ in range(n)]
    # 判断
    ans = set(range(1, m + 1))
    for i in like:
        ans &= i
    # 输出
    print(len(ans))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, m + 1):
        for j in range(n):
            if i in a[j][1:]:
                ans += 1
                break
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    count = 0
    for i in range(1, M+1):
        for j in range(N):
            if i in A[j][1:]:
                count += 1
                break
    print(count)

=======
Suggestion 4

def main():
    # N M
    N, M = map(int, input().split())

    # K_1 A_{11}A_{12}...A_{1K_1}
    # K_2 A_{21}A_{22} ...A_{2K_2}
    # :
    # K_N A_{N1}A_{N2} ...A_{NK_N}
    # 用二维数组表示
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    # 用一个数组表示食物的被喜爱的次数
    # 初始化为0
    food = [0] * M

    # 遍历A数组
    for i in range(N):
        # 遍历A[i]数组，注意下标从1开始
        for j in range(1, A[i][0] + 1):
            food[A[i][j] - 1] += 1

    # 统计food数组中值为N的个数
    count = 0
    for i in range(M):
        if food[i] == N:
            count += 1

    print(count)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    K = []
    A = []
    for i in range(N):
        K.append(list(map(int,input().split()))[1:])
        A += K[i]
    A.sort()
    count = 0
    for i in range(M):
        if A.count(i+1) == N:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    # 读入数据
    N, M = map(int, input().split())
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    # print(N, M)
    # print(type(N), type(M))
    # print(type(N), type(M))
    K = []
    A = []
    for i in range(N):
        temp = list(map(int, input().split()))
        K.append(temp[0])
        A.append(temp[1:])
    # print(K)
    # print(A)
    # print(type(K))
    # print(type(A))
    # print(K[0])
    # print(A[0])
    # print(type(K[0]))
    # print(type(A[0]))
    # print(K[1])
    # print(A[1])
    # print(type(K[1]))
    # print(type(A[1]))
    # print(K[2])
    # print(A[2])
    # print(type(K[2]))
    # print(type(A[2]))
    # print(K[3])
    # print(A[3])
    # print(type(K[3]))
    # print(type(A[3]))
    # print(K[4])
    # print(A[4])
    # print(type(K[4]))

=======
Suggestion 7

def main():
    # 读入数据
    n, m = map(int, input().split())
    #print(n, m)
    #print(type(n), type(m))
    #print(type(n), type(m))
    #print("n = %d, m = %d" % (n, m))
    #print("n = %s, m = %s" % (n, m))
    #print("n = %s, m = %s" % (type(n), type(m)))
    #print("n = %d, m = %d" % (type(n), type(m)))
    #print("n = %d, m = %d" % (str(n), str(m)))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("n = %s, m = %s" % (str(type(n)), str(type(m))))
    #print("n = %d, m = %d" % (str(type(n)), str(type(m))))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("n = %d, m = %d" % (n, m))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("n = %d, m = %d" % (n, m))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("n = %d, m = %d" % (n, m))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("n = %d, m = %d" % (n, m))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("n = %d, m = %d" % (n, m))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("n = %d, m = %d" % (n, m))
    #print("n = %s, m = %s" % (str(n), str(m)))
    #print("

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))

    #print(a)

    b = []
    for i in range(n):
        for j in range(a[i][0]):
            b.append(a[i][j+1])

    #print(b)

    c = [0]*(m+1)
    for i in range(len(b)):
        c[b[i]] += 1

    #print(c)

    count = 0
    for i in range(len(c)):
        if c[i] == n:
            count += 1

    print(count)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    ans = 0
    for _ in range(n):
        k, *a = map(int, input().split())
        ans += len(set(a) & set(range(1, m+1))) == m
    print(ans)

=======
Suggestion 10

def main():
    # 读取数据
    line = input()
    N, M = line.split()
    N = int(N)
    M = int(M)
    #print(N, M)
    #print(type(N), type(M))
    #print(type(line))
    #print(line)
    #print(line.split())
    #print(type(line.split()))
    #print(type(line.split()[0]))
    #print(type(line.split()[1]))
    #print(int(line.split()[0]), int(line.split()[1]))
    #print(type(int(line.split()[0])), type(int(line.split()[1])))
    #print(type(line.split()[0]), type(line.split()[1]))

    #创建一个N行M列的数组，初始值为0
    foods = [[0 for i in range(M)] for j in range(N)]
    #print(foods)
    #print(type(foods))
    #print(foods[0])
    #print(type(foods[0]))
    #print(foods[0][0])
    #print(type(foods[0][0]))
    #print(foods[0][1])
    #print(type(foods[0][1]))
    #print(foods[0][2])
    #print(type(foods[0][2]))
    #print(foods[0][3])
    #print(type(foods[0][3]))
    #print(foods[0][4])
    #print(type(foods[0][4]))
    #print(foods[1])
    #print(type(foods[1]))
    #print(foods[1][0])
    #print(type(foods[1][0]))
    #print(foods[1][1])
    #print(type(foods[1][1]))
    #print(foods[1][2])
    #print(type(foods[1][2]))
    #print(foods[1][3])
    #print(type(foods[1][3]))
    #print(foods[1][4])
    #print(type(foods[1][4]))
    #print(foods[2])
    #print(type(foods[2]))
    #print(foods[2][0])
    #print(type(foods[2][0]))
    #print(foods[2][1])
    #print(type(foods[2][1]))
    #print(foods[2][2])
