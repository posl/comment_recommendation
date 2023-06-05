def main():
    #输入
    N = int(input())
    #处理
    #N是否包含数字7
    #算出百位，十位，个位
    #百位
    N_100 = N//100
    #十位
    N_10 = N%100//10
    #个位
    N_1 = N%10
    #输出
    if N_100 == 7 or N_10 == 7 or N_1 == 7:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()