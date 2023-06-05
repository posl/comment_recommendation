def main():
    print("请输入一个数：")
    N = int(input())
    i = 1
    while i * i <= N:
        i += 1
    print(i - 2 + N // (i - 1) - 1)
    return 0

if __name__ == '__main__':
    main()