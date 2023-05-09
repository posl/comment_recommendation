def main():
    n = int(input())
    a = [[1]]
    for i in range(1, n):
        a.append([1])
        for j in range(1, i):
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])
        a[i].append(1)
    for i in range(n):
        print(*a[i])

if __name__ == '__main__':
    main()