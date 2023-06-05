def get_input():
    N, T = map(int, input().split())
    c_t = []
    for i in range(N):
        c_t.append(list(map(int, input().split())))
    return N, T, c_t

if __name__ == '__main__':
    get_input()