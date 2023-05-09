def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    min = x[0]
    max = x[n-1]
    min_sum = 10000000000
    for i in range(min, max+1):
        sum = 0
        for j in range(n):
            sum += (x[j] - i) ** 2
        if sum < min_sum:
            min_sum = sum
    print(min_sum)

if __name__ == '__main__':
    main()