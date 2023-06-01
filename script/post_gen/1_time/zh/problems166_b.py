Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = [0]*K
    for i in range(K):
        A[i] = list(map(int, input().split()))
    #print(A)
    #print(A[0][0])
    #print(A[0][1])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[0][1])
    #print(A[1][1])

=======
Suggestion 2

def func1():
    n,k=map(int,input().split())
    d=[]
    for i in range(k):
        d.append(int(input()))
        a=list(map(int,input().split()))
    res=n
    for i in range(n):
        for j in range(k):
            if i+1 in a:
                res-=1
                break
    print(res)

=======
Suggestion 3

def main():
    # 读入数据
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    # 算法
    # 1. 初始化
    snuke = [0] * N
    # 2. 遍历
    for i in range(K):
        for j in range(len(A[i])):
            snuke[A[i][j] - 1] += 1
    # 3. 输出
    print(snuke.count(0))

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    snukes = [0 for i in range(n)]
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for i in range(d):
            snukes[a[i]-1] += 1
    print(snukes.count(0))
solve()

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    l = [0] * n
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for j in range(d):
            l[a[j] - 1] += 1
    print(l.count(0))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(K):
            if i+1 not in A[j]:
                count += 1
                break
    print(count)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    a = []
    for _ in range(k):
        a.append(list(map(int, input().split()))[1:])
    a = set(sum(a, []))
    print(n-len(a))

=======
Suggestion 8

def readinput():
    n,k=list(map(int,input().split()))
    d=[]
    a=[]
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int,input().split())))
    return n,k,d,a

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    d = []
    for i in range(k):
        d.append(list(map(int, input().split()))[1:])
    print(n - len(set([x for y in d for x in y])))

main()

=======
Suggestion 10

def main():
    # 读入数据
    n, k = map(int, input().split())
    # 零食的种类
    d = []
    # 零食的编号
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    # 零食的种类
    # print(d)
    # 零食的编号
    # print(a)
    # 零食的编号集合
    a_set = set()
    for i in range(k):
        for j in range(d[i]):
            a_set.add(a[i][j])
    # print(a_set)

    # 受害者的数量
    count = 0
    for i in range(1, n+1):
        if i not in a_set:
            count += 1
    print(count)
