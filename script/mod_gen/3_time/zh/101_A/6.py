def main():
    #读入数据
    s = input()
    #print(s)
    #计算结果
    result = 0
    for i in range(0,4):
        if s[i] == "+":
            result += 1
        else:
            result -= 1
    #输出结果
    print(result)

if __name__ == '__main__':
    main()