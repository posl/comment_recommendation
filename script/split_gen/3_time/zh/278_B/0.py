def main():
    #读取输入
    H, M = map(int, input().split())
    #print(H, M)
    #计算下一个时间
    if M < 59:
        M = M + 1
    elif M == 59:
        M = 0
        if H < 23:
            H = H + 1
        elif H == 23:
            H = 0
    #输出结果
    print('{0:02d} {1:02d}'.format(H, M))
