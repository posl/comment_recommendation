def main():
    #输入
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    #处理
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])

if __name__ == '__main__':
    main()