def main():
    print("请输入两个整数，用空格分隔：")
    a, b = map(int, input().split())
    print(a**b)

if __name__ == '__main__':
    main()