def get_input():
    N, M = map(int, input().split())
    if 2 <= N <= 2 * 10 ** 5 and 0 <= M <= min(2 * 10 ** 5, N * (N - 1) / 2):
        print('N = {}, M = {}'.format(N, M))
    else:
        print('N or M is not in the range')
        exit()
    return N, M
