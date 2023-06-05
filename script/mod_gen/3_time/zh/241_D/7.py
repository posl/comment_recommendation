def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            a.sort()
            if len(a) < query[2]:
                print(-1)
            else:
                print(a[-query[2]])
        else:
            a.sort(reverse = True)
            if len(a) < query[2]:
                print(-1)
            else:
                print(a[-query[2]])

if __name__ == '__main__':
    main()