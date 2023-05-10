def main():
    n,m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    count = 0
    for i in range(1,m+1):
        flg = True
        for j in range(n):
            if i not in a[j]:
                flg = False
        if flg:
            count += 1
    print(count)

if __name__ == '__main__':
    main()