def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    l.append([0, 0])
    count = 1
    for i in range(1, n + 1):
        if l[i - 1] != l[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()