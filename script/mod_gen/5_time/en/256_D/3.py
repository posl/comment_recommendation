def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    start = l[0][0]
    end = l[0][1]
    for i in range(1, n):
        if l[i][0] <= end:
            end = max(end, l[i][1])
        else:
            print(start, end)
            start = l[i][0]
            end = l[i][1]
    print(start, end)

if __name__ == '__main__':
    main()