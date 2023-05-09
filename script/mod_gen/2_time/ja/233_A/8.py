def main():
    x, y = map(int, input().split())
    # 10円切手の枚数
    count = 0
    # 10円切手を貼り付ける
    while x < y:
        x += 10
        count += 1
    print(count)

if __name__ == '__main__':
    main()