def problem125_d():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    minus_count = 0
    min_abs = 10**9 + 1
    for i in range(n):
        sum += abs(a[i])
        if a[i] < 0:
            minus_count += 1
        if min_abs > abs(a[i]):
            min_abs = abs(a[i])
    if minus_count % 2 == 0:
        print(sum)
    else:
        print(sum - 2 * min_abs)
problem125_d()
