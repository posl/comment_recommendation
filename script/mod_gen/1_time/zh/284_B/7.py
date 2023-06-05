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
