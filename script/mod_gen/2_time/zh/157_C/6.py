def get_input():
    # N M
    # s_1 c_1
    # .
    # .
    # .
    # s_M c_M
    N, M = map(int, input().split())
    s_c = []
    for i in range(M):
        s_c.append(list(map(int, input().split())))
    return N, M, s_c

if __name__ == '__main__':
    get_input()