def get_min_num_not_in_a_list(a):
    if not a:
        return 1
    if a[-1] == len(a):
        return len(a) + 1
    for i in range(1, len(a)):
        if a[i] - a[i-1] > 1:
            return a[i-1] + 1

if __name__ == '__main__':
    get_min_num_not_in_a_list()