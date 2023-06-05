def main():
    #输入
    N = int(input())
    S = input()
    #计算ABC出现的次数
    count = 0
    for i in range(N-2):
        if S[i:i+3] == "ABC":
            count += 1
    #输出
    print(count)

if __name__ == '__main__':
    main()