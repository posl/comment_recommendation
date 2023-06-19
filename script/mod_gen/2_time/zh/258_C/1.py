def main():
    # 读入数据
    n, q = map(int, input().split())
    s = list(input())
    # 处理查询
    for i in range(q):
        t, x = input().split()
        if t == "1":
            s = s[-int(x):] + s[:-int(x)]
        else:
            print(s[int(x) - 1])

if __name__ == '__main__':
    main()