def main():
    n = int(input())
    a = [[1]]
    for i in range(n-1):
        a.append([1])
        for j in range(i):
            a[i+1].append(a[i][j]+a[i][j+1])
        a[i+1].append(1)
    for i in range(n):
        print(*a[i])

if __name__ == '__main__':
    main()