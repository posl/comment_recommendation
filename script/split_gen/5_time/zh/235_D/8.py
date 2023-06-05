def main():
    #获取输入
    a,N = input().split()
    a = int(a)
    N = int(N)
    #判断是否可以被10整除
    if N%10 == 0:
        print(-1)
        return
    #将N转换成字符串
    N = str(N)
    #将N转换成整型列表
    N = list(map(int,N))
    #计算最小次数
    count = 0
    while N != [1]:
        #判断是否可以被a整除
        if N[-1]%a == 0:
            N[-1] = N[-1]//a
            N.insert(0,N.pop())
            count += 1
        #不可以被a整除
        else:
            N[-2] += N[-1]*10
            N.pop()
            N[-1] = N[-1]%a
            count += 1
    print(count)
    return
main()
