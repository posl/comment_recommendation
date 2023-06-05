def get_weight(n):
    if n <= 3:
        return [1,2,3]
    elif n % 2 == 0:
        return [1,2] + get_weight(n - 3)
    else:
        return [2,3] + get_weight(n - 5)

if __name__ == '__main__':
    get_weight()