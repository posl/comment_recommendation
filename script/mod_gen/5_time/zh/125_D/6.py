def main():
    n = int(input())
    a = list(map(int, input().split()))
    sign = 1
    a_sum = 0
    min_abs = 10**10
    for i in range(n):
        a_sum += abs(a[i])
        if a[i] < 0:
            sign *= -1
        min_abs = min(min_abs, abs(a[i]))
    if sign == 1:
        print(a_sum)
    else:
        print(a_sum - 2 * min_abs)

if __name__ == '__main__':
    main()