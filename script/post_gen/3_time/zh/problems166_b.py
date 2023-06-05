Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = []
    for i in range(k):
        d[i] = int(input())
        a.append(list(map(int, input().split())))
    a = sum(a, [])
    a = set(a)
    print(n - len(a))

=======
Suggestion 2

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
            if i+1 in a[j]:
                break
        else:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))

    count = 0
    for i in range(n):
        flag = True
        for j in range(k):
            if i+1 not in a[j]:
                flag = False
        if flag:
            count += 1

    print(count)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))

    #print(N, K, d, A)

    cnt = 0
    for i in range(N):
        flag = False
        for j in range(K):
            if i+1 in A[j]:
                flag = True
        if not flag:
            cnt += 1

    print(cnt)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    #print(n,k)
    d = []
    for i in range(k):
        d.append(list(map(int,input().split())))
    #print(d)
    d = [item for sublist in d for item in sublist]
    #print(d)
    d = list(set(d))
    #print(d)
    print(n-len(d))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [[0] * n for i in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        flag = 0
        for j in range(k):
            if i+1 in a[j]:
                flag = 1
        if flag == 0:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def solve():
    n,k = map(int,input().split())
    a = [0] * n
    for i in range(k):
        d = int(input())
        A = list(map(int,input().split()))
        for j in range(d):
            a[A[j]-1] += 1
    cnt = 0
    for i in range(n):
        if a[i] == 0:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    list1 = []
    for i in range(k):
        d = int(input())
        list1.append(list(map(int,input().split())))
    list2 = []
    for i in range(n):
        list2.append(0)
    for i in range(k):
        for j in range(len(list1[i])):
            list2[list1[i][j]-1] += 1
    print(list2.count(0))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    # print(d)
    # print(a)
    # print(n)
    # print(k)
    # print(len(d))
    # print(len(a))
    # print(len(a[0]))
    # print(a[0][0])
    # print(a[0][1])
    # print(a[1][0])
    # print(a[1][1])
    # print(a[1][2])
    # print(a[2][0])
    # print(a[2][1])
    # print(a[2][2])
    # print(a[2][3])
    # print(a[2][4])
    # print(a[2][5])

    # print(d[0])
    # print(d[1])
    # print(d[2])
    # print(d[3])
    # print(d[4])
    # print(d[5])
    # print(d[6])
    # print(d[7])
    # print(d[8])
    # print(d[9])
    # print(d[10])
    # print(d[11])
    # print(d[12])
    # print(d[13])
    # print(d[14])
    # print(d[15])
    # print(d[16])
    # print(d[17])
    # print(d[18])
    # print(d[19])
    # print(d[20])
    # print(d[21])
    # print(d[22])
    # print(d[23])
    # print(d[24])
    # print(d[25])
    # print(d[26])
    # print(d[27])
    # print(d[28])
    # print(d[29])
    # print(d[30])
    # print(d[31])
    # print(d[32])
    # print(d[33])
    # print(d[34])
    # print(d[35])
    # print(d[36])
    # print(d[37])
    # print(d[38])
    # print(d[39])
    # print(d[40])
    # print(d[41])
    # print(d[42])
    # print(d[43])
    # print(d[44])

=======
Suggestion 10

def main():
    pass
