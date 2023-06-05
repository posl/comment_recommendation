def solve(n, a):
    sum = 0
    minus = 0
    absmin = 1000000000
    for i in range(n):
        sum += abs(a[i])
        if a[i] < 0:
            minus += 1
        if abs(a[i]) < absmin:
            absmin = abs(a[i])
    if minus % 2 == 0:
        return sum
    else:
        return sum - 2*absmin
