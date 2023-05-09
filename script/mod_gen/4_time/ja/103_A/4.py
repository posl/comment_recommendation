def main():
    # 自分の解答
    # a = list(map(int, input().split()))
    # a.sort()
    # print(a[2]-a[0])
    # 解答例1
    a = list(map(int, input().split()))
    print(max(a) - min(a))

if __name__ == '__main__':
    main()