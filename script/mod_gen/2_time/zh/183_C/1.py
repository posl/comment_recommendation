def get_time(n, k, T):
    count = 0
    for i in range(n):
        if T[0][i] == 0:
            continue
        else:
            count += T[0][i] + get_time_helper(n, k, T, i, 1, [0, i])
    return count

if __name__ == '__main__':
    get_time()