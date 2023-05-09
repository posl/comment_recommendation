def get_cnt(N):
    # 9^5 = 59049
    # 6^6 = 46656
    if N <= 5:
        return N
    if N <= 59049:
        return get_cnt(N - 59049) + 1
    if N <= 46656:
        return get_cnt(N - 46656) + 1
    if N <= 59049 + 46656:
        return get_cnt(N - 59049 - 46656) + 2
    return get_cnt(N - 59049 - 46656 - 59049) + 3

if __name__ == '__main__':
    get_cnt()