def get_max_remainder_sum(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n * (n - 1)) // 2

if __name__ == '__main__':
    get_max_remainder_sum()