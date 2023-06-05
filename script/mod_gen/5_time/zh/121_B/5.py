def main():
    n = 2
    m = 3
    c = -10
    b = [1,2,3]
    a = [[3,2,1],[1,2,2]]
    count = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += a[i][j] * b[j]
        sum += c
        if sum > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()