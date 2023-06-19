Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(k)
    b = [0]
    for i in range(n):
        b.append(a[i+1]-a[i])
    b.sort()
    print(sum(b[0:n-1]))

main()

=======
Suggestion 2

def main():
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    A.append(K)
    A.append(0)
    A.sort()
    max = 0
    for i in range(N):
        if A[i+1]-A[i] > max:
            max = A[i+1]-A[i]
    print(K-max)

=======
Suggestion 3

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    ans = k
    for i in range(n):
        ans = min(ans, k - (a[i+1]-a[i]))
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    ans = k
    for i in range(n):
        if i == n-1:
            ans = min(ans,k-a[i]+a[0])
        else:
            ans = min(ans,a[i+1]-a[i])
    print(ans)

=======
Suggestion 6

def main():
    print("请分别输入池塘周长和房子的个数：")
    K,N = map(int,input().split())
    print("请输入各个房子离池塘的距离：")
    A = list(map(int,input().split()))
    #print(A)
    #print(K,N)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #

=======
Suggestion 7

def main():
    # 输入
    K, N = map(int, input().split())
    A = list(map(int, input().split()))

    # 初始化
    max_dis = 0
    for i in range(N - 1):
        dis = A[i + 1] - A[i]
        if dis > max_dis:
            max_dis = dis
    dis = K - A[N - 1] + A[0]
    if dis > max_dis:
        max_dis = dis

    # 输出
    print(K - max_dis)

=======
Suggestion 8

def main():
    #读取输入
    K,N = map(int,input().split())
    A = list(map(int,input().split()))
    #计算最大距离
    max_distance = 0
    for i in range(N-1):
        max_distance = max(max_distance,A[i+1]-A[i])
    #计算最小距离
    min_distance = K - A[N-1] + A[0]
    for i in range(N-1):
        min_distance = min(min_distance,A[i+1]-A[i])
    #计算答案
    print(K - max_distance - min_distance)
