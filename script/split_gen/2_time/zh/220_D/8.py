def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    x = int(input())
    x_10_100 = x * 10**100
    sum_a = sum(a)
    sum_b = sum_a * 10**100
    if sum_b <= x_10_100:
        print(10**100)
        return
    sum_b = 0
    k = 0
    while True:
        sum_b += a[k % n]
        if sum_b > x_10_100:
            break
        k += 1
    print(k + 1)
