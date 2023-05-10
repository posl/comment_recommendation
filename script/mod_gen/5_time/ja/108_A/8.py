def calc_even_odd_pairs(n):
    if n % 2 == 0:
        return int(n/2) * int(n/2)
    else:
        return int(n/2) * (int(n/2) + 1)

if __name__ == '__main__':
    calc_even_odd_pairs()