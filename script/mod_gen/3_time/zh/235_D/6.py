def problem235_d(a, N):
    if N % a == 0:
        return -1
    count = 0
    while N > 0:
        if N % a == 1:
            N = (N - 1) // a
        else:
            N -= 1
        count += 1
    return count

if __name__ == '__main__':
    problem235_d()