def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    max_sum = 0
    for i in range(n - m + 1):
        sum = 0
        for j in range(m):
            sum += (j + 1) * a[i + j]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)

if __name__ == '__main__':
    main()