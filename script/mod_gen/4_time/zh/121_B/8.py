def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += b[j] * a[i][j]
        sum += c
        if sum > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()