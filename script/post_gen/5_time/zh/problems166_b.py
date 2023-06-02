Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    d = []
    for i in range(k):
        d.append(list(map(int, input().split()))[1:])
    print(n - len(set(sum(d, []))))

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int,input().split())))
    #print(N,K,d,A)
    count = 0
    for i in range(N):
        flag = 0
        for j in range(K):
            if i+1 in A[j]:
                flag = 1
                break
        if flag == 0:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    d = []
    for i in range(k):
        d.append(int(input()))
        d.append(list(map(int,input().split())))
    #print(d)
    count = 0
    for i in range(1,n+1):
        flag = 0
        for j in range(1,len(d),2):
            if i in d[j]:
                flag = 1
                break
        if flag == 0:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    S = set()
    for i in range(K):
        for j in range(d[i]):
            S.add(A[i][j])
    print(N - len(S))

=======
Suggestion 5

def countSnukes(n, k, d, A):
    snukes = [0 for i in range(n)]
    for i in range(k):
        for j in range(d[i]):
            snukes[A[i][j] - 1] += 1
    return snukes.count(0)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    snuke = [0] * n
    for i in range(k):
        for j in range(d[i]):
            snuke[a[i][j] - 1] = 1
    print(snuke.count(0))

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = [0] * n
    for i in range(k):
        d = int(input())
        A = list(map(int,input().split()))
        for j in range(d):
            a[A[j]-1] += 1
    ans = 0
    for i in range(n):
        if a[i] == 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(k):
            if i + 1 in a[j]:
                break
            if j == k - 1:
                cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    d = [0]*k
    a = [0]*k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int,input().split()))
    ans = n
    for i in range(k):
        for j in range(d[i]):
            if a[i][j] == ans:
                ans -= 1
    print(ans)

=======
Suggestion 10

def main():
    # 读入数据
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    # 初始化
    Snukes = [0] * N
    # 计算
    for i in range(K):
        for j in range(d[i]):
            Snukes[A[i][j]-1] += 1
    # 输出
    print(Snukes.count(0))
