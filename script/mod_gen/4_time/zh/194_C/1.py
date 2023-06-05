def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += (n - i - 1) * a[i] ** 2
        sum -= (n - i - 1) * a[i] * 2 * sum
    print(sum)

if __name__ == '__main__':
    main()