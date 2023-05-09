def calc_sum(a):
    sum = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            sum = sum + a[i] * a[j]
    return sum
