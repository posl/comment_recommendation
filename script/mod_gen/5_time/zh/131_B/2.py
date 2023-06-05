def main():
    #读取数据
    n, l = map(int, input().split())
    #计算最佳选择
    if l > 0:
        print(sum(range(l+1, l+n)))
    elif l+n-1 < 0:
        print(sum(range(l, l+n-1, -1)))
    else:
        print(sum(range(l, l+n)))

if __name__ == '__main__':
    main()