def confusing_time(H, M):
    if H == 23 and M > 32:
        H = 0
        M = 0
    elif M > 32:
        H += 1
        M = 0
    else:
        M += 1
    return H, M

if __name__ == '__main__':
    confusing_time()