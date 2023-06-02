Synthesizing 10/10 solutions

=======
Suggestion 1

def get_count_of_triplets(A):
    N = len(A)
    count = 0
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    count += 1
    return count

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N-1):
        for j in range(i+1, N):
            if A[i-1] != A[j-1]:
                cnt += N-j
                break
    print(cnt)
    return

=======
Suggestion 3

def main():
    n = int(input())
    A = list(map(int,input().split()))

    A.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    if A[i] + A[j] > A[k]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #先找出所有满足条件的三元组
    #1≦ i < j < k ≦ N
    #A_i, A_j, and A_k是不同的。
    #满足条件的三元组个数为：
    #C(N, 3) = N! / (3! * (N-3)!)
    # = (N * (N-1) * (N-2) * (N-3)!) / (3! * (N-3)!)
    # = N * (N-1) * (N-2) / 6
    # = N * (N-1) * (N-2) / 6
    # = (N^3 - 3N^2 + 2N) / 6
    # = (N * (N-1) * (N-2)) / 6
    # = N * (N-1) * (N-2) / 6
    # = (N^3 - 3N^2 + 2N) / 6
    # = (N * (N-1) * (N-2)) / 6
    # = N * (N-1) * (N-2) / 6
    # = (N^3 - 3N^2 + 2N) / 6
    # = (N * (N-1) * (N-2)) / 6
    # = N * (N-1) * (N-2) / 6
    # = (N^3 - 3N^2 + 2N) / 6
    # = (N * (N-1) * (N-2)) / 6
    # = N * (N-1) * (N-2) / 6
    # = (N^3 - 3N^2 + 2N) / 6
    # = (N * (N-1) * (N-2)) / 6
    # = N * (N-1) * (N-2) / 6

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[i] == a[k] or a[j] == a[k]:
                    continue
                if a[i] + a[j] > a[k]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    #print(n)
    b = [0 for i in range(200001)]
    #print(b)
    for i in range(n):
        b[a[i]] += 1
    #print(b)
    c = [0 for i in range(200001)]
    #print(c)
    for i in range(200000):
        c[i + 1] = c[i] + b[i]
    #print(c)
    ans = 0
    for i in range(200000):
        if b[i] > 1:
            ans += b[i] * (b[i] - 1) // 2 * (c[i] - b[i])
        if b[i] > 2:
            ans += b[i] * (b[i] - 1) * (b[i] - 2) // 6
    print(ans)

=======
Suggestion 8

def solve(N, A):
    ans = 0
    # 从左侧开始
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 4 5 6 7 8 9 10

    # 从右侧开始
    # 10 9 8 7 6 5 4 3 2 1
    # 10 9 8 7 6 5 4 3 2 1
    # 10 9 8 7 6 5 4 3 2 1

    # 从左侧开始
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 4 5 6 7 8 9 10

    # 从右侧开始
    # 10 9 8 7 6 5 4 3 2 1
    # 10 9 8 7 6 5 4 3 2 1
    # 10 9 8 7 6 5 4 3 2 1

    # 从左侧开始
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 4 5 6 7 8 9 10

    # 从右侧开始
    # 10 9 8 7 6 5 4 3 2 1
    # 10 9 8 7 6 5 4 3 2 1
    # 10 9 8 7 6 5 4 3 2 1

    # 从左侧开始
    # 1 2 3 4 5

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n, a)
    #print(len(a))
    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])
    #print(a[55])
    #print(a[56])
    #print(a[57])
    #print(a[58])
    #print(a[59])
    #print(a[60])
    #print(a[61])
    #print(a[62])
    #print(a[63])
    #print(a[64])
    #print(a[65])
    #print(a[66
