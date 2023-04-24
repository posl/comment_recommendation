Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    #print(A)
    #print(B)
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    #print(D)
    for i in range(N):
        D[i + 1] += D[i]
    #print(D)
    D = D[1:]
    #print(D)
    D = [str(x) for x in D]
    print(' '.join(D))

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(N):
        D[i + 1] += D[i]
    del D[0]
    print(" ".join(map(str, D)))

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0] * N
    for i in range(N):
        D[0] += B[i] - 1
        D[i] += 1
        if i < N - 1:
            D[i + 1] += A[i + 1] - (A[i] + B[i]) - 1
    print(*D, sep=" ")

=======
Suggestion 4

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    print(" ".join(map(str, D[1:])))

=======
Suggestion 5

def main():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    D = D[1:]
    print(" ".join(map(str, D)))

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    D = [0]*N
    for i in range(N):
        D[0] += B[i]
        if i != N-1:
            D[i+1] -= A[i+1] - (A[i] + B[i] - 1)
    for i in range(1,N):
        D[i] += D[i-1]
    print(*D)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(A)
    #print(B)
    #print(A[0])
    #print(B[0])
    #print(A[1])
    #print(B[1])
    #print(A[2])
    #print(B[2])
    #print(A[3])
    #print(B[3])
    #print(A[4])
    #print(B[4])
    #print(A[5])
    #print(B[5])
    #print(A[6])
    #print(B[6])
    #print(A[7])
    #print(B[7])
    #print(A[8])
    #print(B[8])
    #print(A[9])
    #print(B[9])
    #print(A[10])
    #print(B[10])
    #print(A[11])
    #print(B[11])
    #print(A[12])
    #print(B[12])
    #print(A[13])
    #print(B[13])
    #print(A[14])
    #print(B[14])
    #print(A[15])
    #print(B[15])
    #print(A[16])
    #print(B[16])
    #print(A[17])
    #print(B[17])
    #print(A[18])
    #print(B[18])
    #print(A[19])
    #print(B[19])
    #print(A[20])
    #print(B[20])
    #print(A[21])
    #print(B[21])
    #print(A[22])
    #print(B[22])
    #print(A[23])
    #print(B[23])
    #print(A[24])
    #print(B[24])
    #print(A[25])
    #print(B[25])
    #print(A[26])
    #print(B[26])
    #print(A[27])
    #print(B[27])
    #print(A[28])
    #print(B[28])
    #print(A[29])
    #print(B[29])
    #print(A[30])
    #print(B

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    d = [0] * (10 ** 9 + 2)
    for i in range(n):
        d[a[i]] += 1
        d[a[i] + b[i]] -= 1
    #print(d)
    for i in range(1, 10 ** 9 + 2):
        d[i] += d[i - 1]
    #print(d)
    ans = [0] * (n + 1)
    for i in range(10 ** 9 + 2):
        ans[d[i]] += 1
    #print(ans)
    for i in range(1, n + 1):
        print(ans[i], end = " ")
    print()

=======
Suggestion 9

def main():
    N = int(input())
    # A_i と B_i を格納する配列を用意
    A = []
    B = []
    for i in range(N):
        # A_i, B_i をスペース区切りで受け取る
        A_i, B_i = map(int, input().split())
        # A_i, B_i をそれぞれ配列に格納
        A.append(A_i)
        B.append(B_i)
    # D_i を格納する配列を用意
    D = [0] * N
    # 1 人がログインしている日数を格納する配列を用意
    one = [0] * (10 ** 9 + 1)
    # 2 人がログインしている日数を格納する配列を用意
    two = [0] * (10 ** 9 + 1)
    # 3 人がログインしている日数を格納する配列を用意
    three = [0] * (10 ** 9 + 1)
    # 1 人がログインしている日数を計算
    for i in range(N):
        one[A[i]] += 1
        one[A[i] + B[i]] -= 1
    # 1 人がログインしている日数の累積和を計算
    for i in range(1, 10 ** 9 + 1):
        one[i] += one[i - 1]
    # 2 人がログインしている日数を計算
    for i in range(N):
        if one[A[i]] >= 2:
            two[A[i]] += 1
            two[A[i] + B[i]] -= 1
    # 2 人がログインしている日数の累積和を計算
    for i in range(1, 10 ** 9 + 1):
        two[i] += two[i - 1]
    # 3 人がログインしている日数を計算
    for i in range(N):
        if two[A[i]] >= 1:

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort()
    #print(AB)
    #print("AB[0][1]=", AB[0][1])
    D = [0] * N
    #print("D=", D)
    for i in range(1, N):
        #print("i=", i)
        if AB[i][0] <= AB[i-1][0] + AB[i-1][1] - 1:
            #print("AB[i][0]=", AB[i][0], "AB[i-1][0]=", AB[i-1][0], "AB[i-1][1]=", AB[i-1][1])
            #print("AB[i][0]=", AB[i][0], "AB[i-1][0] + AB[i-1][1] - 1=", AB[i-1][0] + AB[i-1][1] - 1)
            AB[i][1] = AB[i][1] - (AB[i-1][0] + AB[i-1][1] - AB[i][0])
            AB[i][0] = AB[i-1][0] + AB[i-1][1]
            #print("AB[i][0]=", AB[i][0], "AB[i][1]=", AB[i][1])
    #print(AB)
    for i in range(N):
        D[i] = AB[i][1]
    #print("D=", D)
    for i in range(1, N):
        D[i] += D[i-1]
    #print("D=", D)
    for i in range(N):
        D[i] = D[i] + 10**100 - AB[i][0] - AB[i][1] + 1
    #print("D=", D)
    print(*D)
