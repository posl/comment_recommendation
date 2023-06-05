def get_k(a, x):
    sum_a = sum(a)
    if sum_a > x:
        return 1
    k = 1
    while True:
        sum_a *= 2
        k *= 2
        if sum_a > x:
            break
    k //= 2
    sum_a //= 2
    while k > 0:
        if sum_a + a[k - 1] <= x:
            sum_a += a[k - 1]
        else:
            pass
        k //= 2
    return sum_a

if __name__ == '__main__':
    get_k()