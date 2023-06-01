Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        a = list(map(int,input().split()))
        cnt = 0
        for j in range(m):
            if a[j] % 2 != 0:
                cnt += 1
        print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    # T = int(input())
    T = 4
    # for i in range(T):
    #     N = int(input())
    #     A = list(map(int,input().split()))
    #     # A = [1, 2, 3]
    #     count = 0
    #     for i in A:
    #         if i % 2 != 0:
    #             count += 1
    #     print(count)
    #     # print(A)
    #     # print(N)
    #     # print(A)
    #     # print(A[0])
    #     # print(A[1])
    #     # print(A[2])
    #     # print(A[3])
    #     # print(A[4])
    #     # print(A[5])
    #     # print(A[6])
    #     # print(A[7])
    #     # print(A[8])
    #     # print(A[9])
    #     # print(A[10])
    #     # print(A[11])
    #     # print(A[12])
    #     # print(A[13])
    #     # print(A[14])
    #     # print(A[15])
    #     # print(A[16])
    #     # print(A[17])
    #     # print(A[18])
    #     # print(A[19])
    #     # print(A[20])
    #     # print(A[21])
    #     # print(A[22])
    #     # print(A[23])
    #     # print(A[24])
    #     # print(A[25])
    #     # print(A[26])
    #     # print(A[27])
    #     # print(A[28])
    #     # print(A[29])
    #     # print(A[30])
    #     # print(A[31])
    #     # print(A[32])
    #     # print(A[33])
    #     # print(A[34])
    #     # print(A[35])
    #     # print(A[36])
    #     # print(A[37])
    #     # print(A[38])
    #     # print(A[39])
    #     # print(A[40])
    #     # print(A[41])

=======
Suggestion 4

def odd_number(num):
    count = 0
    for i in range(num):
        if num[i] % 2 == 1:
            count += 1
    return count

=======
Suggestion 5

def problems284_b():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(_) for _ in input().split()]
        count = 0
        for j in range(N):
            if A[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 6

def odd_number_count():
    n = int(input())
    a = list(map(int, input().split()))
    odd_count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            odd_count += 1
    print(odd_count)

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(n):
        a = input()
        b = input()
        c = b.split()
        d = 0
        for j in c:
            if int(j) % 2 != 0:
                d += 1
        print(d)
main()

=======
Suggestion 8

def odd_num():
    #输入测试案例数
    T = int(input())
    #定义一个列表用来存储奇数
    odd_list = []
    #循环输入测试案例
    for i in range(T):
        #输入正整数个数
        N = int(input())
        #输入正整数
        A = input().split()
        #循环判断是否为奇数
        for j in range(N):
            if int(A[j])%2 != 0:
                odd_list.append(A[j])
        #输出奇数个数
        print(len(odd_list))
        #清空列表
        odd_list = []
odd_num()

=======
Suggestion 9

def main():
    # 读取数据
    t = int(input())
    n = []
    a = []
    for i in range(t):
        n.append(int(input()))
        a.append(list(map(int, input().split())))

    # 处理数据
    for i in range(t):
        count = 0
        for j in range(n[i]):
            if a[i][j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 10

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = input().split()
        count = 0
        for j in range(N):
            if int(A[j]) % 2 == 1:
                count += 1
        print(count)
