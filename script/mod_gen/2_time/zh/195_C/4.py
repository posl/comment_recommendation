def num_of_comma(n):
    n_str = str(n)
    len_n = len(n_str)
    if len_n <= 3:
        return 0
    else:
        num = 0
        for i in range(len_n//3):
            num += 1
        return num-1

if __name__ == '__main__':
    num_of_comma()