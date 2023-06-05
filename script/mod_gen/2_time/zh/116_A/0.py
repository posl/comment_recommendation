def get_num_of_patty(n, x):
    if n == 0:
        return 0
    elif x == 1 and n == 1:
        return 0
    elif x <= 1 + get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return get_num_of_patty(n - 1, x - 1)
    elif x == 2 + get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return 1 + get_num_of_patty(n - 1, x - 2)
    elif x <= 2 + 2 * get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return 1 + get_num_of_patty(n - 1, x - 2)
    elif x == 3 + 2 * get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return 2 + get_num_of_patty(n - 1, x - 3)
    else:
        return 2 + get_num_of_patty(n - 1, x - 3)

if __name__ == '__main__':
    get_num_of_patty()