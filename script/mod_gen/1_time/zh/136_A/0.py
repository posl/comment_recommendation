def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 从瓶子2转移到瓶子1
    if b >= a:
        print(c)
    else:
        print(c - (a - b))

if __name__ == '__main__':
    main()