def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    count_minus = 0
    min = 10**9
    for i in range(n):
        if a[i] < 0:
            count_minus += 1
            a[i] *= -1
        sum += a[i]
        if min > a[i]:
            min = a[i]
    if count_minus % 2 == 0:
        print(sum)
    else:
        print(sum - min * 2)

if __name__ == '__main__':
    main()