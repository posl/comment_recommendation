def main():
    #读取数据
    n = int(input())
    #处理数据
    x = 0
    while True:
        x += 1
        if (x*(x+1)//2) >= n:
            break
    #输出数据
    print(x)
    return

if __name__ == '__main__':
    main()