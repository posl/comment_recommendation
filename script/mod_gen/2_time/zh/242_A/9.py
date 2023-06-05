def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            a.sort()
            if query[1] in a:
                print(a[-query[2]])
            else:
                print(-1)
        elif query[0] == 3:
            a.sort()
            if query[1] in a:
                print(a[query[2]-1])
            else:
                print(-1)
        else:
            print("error")
    return 0

if __name__ == '__main__':
    main()