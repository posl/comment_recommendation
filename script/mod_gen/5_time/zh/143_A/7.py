def calc_remainder_of_window(A, B):
    if A <= B:
        return 0
    else:
        return A - B * 2

if __name__ == '__main__':
    calc_remainder_of_window()