def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))
    #处理
    a_max = max(a)
    a_min = min(a)
    max = a_max - a_min
    #输出
    print(max)

if __name__ == '__main__':
    main()