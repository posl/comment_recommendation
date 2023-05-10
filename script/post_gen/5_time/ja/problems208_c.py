Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #N,K = 2,7
    #A = [1,8]
    #N,K = 1,3
    #A = [33]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]

    #A.sort()
    #print(A)
    #print(K)
    #print(N)
    #print(A[0])
    #print(K//N)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = k // n
    k %= n
    b = sorted(a)
    for i in range(k):
        ans[b[i]-1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(K):
        ans[A[i]-1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    a = sorted(A)
    b = K // N
    c = K % N

    for i in range(N):
        if i < c:
            print(b+1)
        else:
            print(b)

=======
Suggestion 5

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # 1人あたりの配るお菓子の数
    # 高橋くんが配るお菓子の数をxとすると、
    # x * n <= k かつ (x+1) * n > k のとき、xが答え
    # これを二分探索で探す
    l = 0
    r = k // n + 1
    while l + 1 < r:
        m = (l + r) // 2
        if m * n <= k and (m+1) * n > k:
            l = m
        elif m * n > k:
            r = m
        else:
            l = m
    x = l

    # 高橋くんが配るお菓子の数がxのとき、
    # 高橋くんが配るお菓子の数がx-1のときに配るお菓子の数はx-1より大きくなる
    # よって、国民番号が小さい方からK'人に1個ずつ配るとき、
    # a_iの値が小さい方からK'人を選び、選んだ人に1個ずつお菓子を配る
    # という操作を、x回行えばよい
    # 高橋くんが配るお菓子の数がxのときに配るお菓子の数はx
    # よって、高橋くんが配るお菓子の数xからx-1までのx回の操作を行えばよい
    # この操作を行った後、高橋くんが配るお菓子の数がx-1のときに配るお菓子の数はx-1より大きくなる
    # よって、残った

=======
Suggestion 6

def calc(n, k, a):
    if n >= k:
        return [1 for i in range(n)]
    else:
        k = k % n
        a.sort()
        result = [0 for i in range(n)]
        for i in range(k):
            result[a[i][1]] += 1
        return result

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_s = sorted(a)
    # print(a_s)
    # print(n, k)
    # print(a)
    # print(a_s)
    # print(a_s[0])
    # print(a_s[1])
    # print(a_s[2])
    # print(a_s[3])
    # print(a_s[4])
    # print(a_s[5])
    # print(a_s[6])
    # print(a_s[7])
    # print(a_s[8])
    # print(a_s[9])
    # print(a_s[10])
    # print(a_s[11])
    # print(a_s[12])
    # print(a_s[13])
    # print(a_s[14])
    # print(a_s[15])
    # print(a_s[16])
    # print(a_s[17])
    # print(a_s[18])
    # print(a_s[19])
    # print(a_s[20])
    # print(a_s[21])
    # print(a_s[22])
    # print(a_s[23])
    # print(a_s[24])
    # print(a_s[25])
    # print(a_s[26])
    # print(a_s[27])
    # print(a_s[28])
    # print(a_s[29])
    # print(a_s[30])
    # print(a_s[31])
    # print(a_s[32])
    # print(a_s[33])
    # print(a_s[34])
    # print(a_s[35])
    # print(a_s[36])
    # print(a_s[37])
    # print(a_s[38])
    # print(a_s[39])
    # print(a_s[40])
    # print(a_s[41])
    # print(a_s[42])
    # print(a_s[43])
    # print(a_s[44])
    # print(a_s[45])
    # print(a_s[46])
    # print(a_s[47])
    # print(a_s[48])
    # print(a_s[49])
    # print(a_s[50])
    # print(a_s[51])
    # print(a_s[52])
    # print(a_s[53])
    # print(a_s[54])
    # print(a

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    C = [0 for _ in range(N)]
    for i in range(N):
        B[i] = i, A[i]
    B.sort(key=lambda x: x[1])
    for i in range(N):
        C[B[i][0]] = i
    cnt = K // N
    K = K % N
    for i in range(N):
        if K > 0:
            print(cnt + 1)
            K -= 1
        else:
            print(cnt)
    return

=======
Suggestion 9

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    #N,K = 2,7
    #A = [1,8]
    #N,K = 1,3
    #A = [33]
    #N,K = 7,1000000000000
    #A = [99,8,2,4,43,5,3]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,9,10]
    #N,K = 10,1000000000000
    #A = [10,9,8,7,6,5,4,3,2,1]
    #N,K = 10,1000000000000
    #A = [1,3,5,7,9,2,4,6,8,10]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,10,9]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,9,10]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,9,10]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,9,10]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,9,10]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,9,10]
    #N,K = 10,1000000000000
    #A = [1,2,3,4,5,6,7,8,9,10]

    #N,K = 2,7
    #A = [1,

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0 for i in range(N)]
    for i in range(N):
        b[a[i]-1] = i
    c = [0 for i in range(N)]
    for i in range(N):
        c[i] = K//N
    for i in range(K%N):
        c[b[i]] += 1
    for i in range(N):
        print(c[i])
