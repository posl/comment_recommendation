def main():
    #读取输入
    S = input()
    T = input()
    #判断S与T的长度
    len_S = len(S)
    len_T = len(T)
    #判断S与T的长度是否符合约束
    if 1 <= len_S <= 5*10**5 and 1 <= len_T <= 5*10**5:
        #判断S与T的长度是否相等
        if len_S == len_T - 1:
            #遍历S
            for i in range(len_S):
                #判断S与T的第i个字符是否相同
                if S[i] != T[i]:
                    #输出i+1
                    print(i+1)
                    #跳出循环
                    break
            else:
                #输出len_T
                print(len_T)
        else:
            #输出len_T
            print(len_T)
    else:
        #输出len_T
        print(len_T)
