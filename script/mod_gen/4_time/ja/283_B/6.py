def main():
    n = int(input())
    a = list(map(int, input().split())) # スペース区切り連続数字
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a[query[1]-1] = query[2]
        elif query[0] == 2:
            print(a[query[1]-1])

if __name__ == '__main__':
    main()