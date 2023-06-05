def main():
    #输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #处理
    for i in range(k):
        a.pop(0)
        a.append(0)
    #输出
    print(" ".join(map(str, a)))

if __name__ == '__main__':
    main()