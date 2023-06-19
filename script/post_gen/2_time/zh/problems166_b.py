Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = []
    for i in range(k):
        d = int(input())
        a.append(list(map(int, input().split())))

    print(n - len(set(sum(a, []))))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    snuke = [0] * n
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for j in range(d):
            snuke[a[j] - 1] += 1
    cnt = 0
    for i in range(n):
        if snuke[i] == 0:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    #print(n, k, d, a)
    #print(len(d), len(a))
    #print(d[0], a[0][0])
    #print(d[1], a[1][0])
    #print(d[2], a[2][0])
    #print(a[0][0], a[1][0], a[2][0])
    #print(a[0][1], a[1][1], a[2][1])
    #print(a[0][2], a[1][2], a[2][2])
    #print(a[0][0], a[0][1], a[0][2])
    #print(a[1][0], a[1][1], a[1][2])
    #print(a[2][0], a[2][1], a[2][2])
    #print(a[0][0], a[1][0], a[2][0])
    #print(a[0][1], a[1][1], a[2][1])
    #print(a[0][2], a[1][2], a[2][2])
    #print(a[0][0], a[0][1], a[0][2])
    #print(a[1][0], a[1][1], a[1][2])
    #print(a[2][0], a[2][1], a[2][2])
    #print(a[0][0], a[1][0], a[2][0])
    #print(a[0][1], a[1][1], a[2][1])
    #print(a[0][2], a[1][2], a[2][2])
    #print(a[0][0], a[0][1], a[0][2])
    #print(a[1][0], a[1][1], a[1][2])
    #print(a[2][0], a[2][1], a[2][2])
    #print(a[0][0], a[1][0], a[

=======
Suggestion 4

def main():
    n,k=map(int,input().split())
    a=[]
    for i in range(k):
        a.append(list(map(int,input().split())))
    #print(a)
    b=[0 for i in range(n)]
    #print(b)
    for i in range(k):
        for j in range(len(a[i])):
            b[a[i][j]-1]+=1
    #print(b)
    count=0
    for i in range(n):
        if b[i]==0:
            count+=1
    print(count)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [[] for _ in range(K)]
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    S = [0] * N
    for i in range(K):
        for j in range(d[i]):
            S[A[i][j]-1] += 1
    ans = 0
    for i in range(N):
        if S[i] == 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    #print(d)
    #print(a)
    ans = 0
    for i in range(n):
        for j in range(k):
            if i+1 not in a[j]:
                ans += 1
    print(ans)
    return

=======
Suggestion 7

def main():
    # N,K = map(int,input().split())
    # A = []
    # for i in range(K):
    #     d = int(input())
    #     A.append(list(map(int,input().split())))
    N,K = 3,3
    A = [[1,3],[1],[3]]
    A = [sorted(a) for a in A]
    print(A)
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(K):
            if i+1 in A[j]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    n, k = map(int, input().split())
    d = []
    for _ in range(k):
        d.append(int(input()))
        d.extend(list(map(int, input().split())))

    # print(n, k, d)

    # 初始值
    snuke = []
    for i in range(n):
        snuke.append(i + 1)

    # print(snuke)

    # 遍历
    for i in range(k):
        for j in range(d[i]):
            if snuke[j] == d[i + 1 + j]:
                snuke[j] = 0

    # print(snuke)

    # 输出
    print(snuke.count(0))

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    flag = [0 for i in range(n)]
    for i in range(k):
        for j in range(d[i]):
            flag[a[i][j]-1] += 1
    ans = 0
    for i in range(n):
        if flag[i] == 0:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    snuke = [0 for i in range(n)]
    for i in range(k):
        d = int(input())
        a = list(map(int,input().split()))
        for j in range(d):
            snuke[a[j]-1] += 1
    count = 0
    for i in range(n):
        if snuke[i] == 0:
            count += 1
    print(count)
