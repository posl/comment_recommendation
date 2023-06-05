Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    d = [0] * K
    A = []
    for i in range(K):
        d[i] = int(input())
        A.append(list(map(int, input().split())))

    cnt = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            cnt += 1

    print(cnt)
solve()

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    d = [0 for i in range(k)]
    a = [[0 for i in range(n)] for j in range(k)]

    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        flag = False
        for j in range(k):
            if i+1 in a[j]:
                flag = True
        if not flag:
            cnt += 1

    print(cnt)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    S = [0] * N
    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for a in A:
            S[a-1] += 1
    print(S.count(0))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    d = []
    for i in range(k):
        d.append(list(map(int, input().split()))[1:])
    print(n - len(set(sum(d, []))))

=======
Suggestion 5

def main():
    #input
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        A.append(list(map(int, input().split()))[1:])

    #calc
    Snuke = [0 for i in range(N)]
    for i in range(K):
        for j in range(len(A[i])):
            Snuke[A[i][j]-1] += 1

    #output
    count = 0
    for i in range(N):
        if Snuke[i] == 0:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())

    # 零食的集合
    snacks = set()
    for i in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for j in range(d):
            snacks.add(a[j])

    # 没有零食的人
    no_snacks = n - len(snacks)
    print(no_snacks)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = []
    for i in range(k):
        a.append(list(map(int, input().split())))

    snuke = [0] * n
    for i in range(k):
        for j in range(a[i][0]):
            snuke[a[i][j + 1] - 1] += 1

    print(snuke.count(0))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        A.append(list(map(int, input().split())))
    #print(A)
    #print(N, K)
    #print(A[0][0])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[2][2])
    #print(A[2][3])
    #print(A[2][4])
    #print(A[2][5])
    #print(A[2][6])
    #print(A[2][7])
    #print(A[2][8])
    #print(A[2][9])
    #print(A[2][10])
    #print(A[2][11])
    #print(A[2][12])
    #print(A[2][13])
    #print(A[2][14])
    #print(A[2][15])
    #print(A[2][16])
    #print(A[2][17])
    #print(A[2][18])
    #print(A[2][19])
    #print(A[2][20])
    #print(A[2][21])
    #print(A[2][22])
    #print(A[2][23])
    #print(A[2][24])
    #print(A[2][25])
    #print(A[2][26])
    #print(A[2][27])
    #print(A[2][28])
    #print(A[2][29])
    #print(A[2][30])
    #print(A[2][31])
    #print(A[2][32])
    #print(A[2][33])
    #print(A[2][34])
    #print(A[2][35])
    #print(A[2][36])
    #print(A[2][37])
    #print(A[2][38])
    #print(A[2][39])
    #print(A[2][40])
    #print(A[2][41])
    #print(A[2][42])
    #print(A[2][43])
    #print(A[2][44])
    #print(A[2][45])
    #

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    d = [0]*K
    A = []
    for i in range(K):
        d[i] = int(input())
        A.append(list(map(int,input().split())))
    S = [0]*N
    for i in range(K):
        for j in range(d[i]):
            S[A[i][j]-1] = 1
    print(S.count(0))

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    d = [0]*k
    a = [0]*k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int,input().split()))
    snuke = [0]*n
    for i in range(k):
        for j in range(d[i]):
            snuke[a[i][j]-1] += 1
    ans = 0
    for i in range(n):
        if snuke[i] == 0:
            ans += 1
    print(ans)
