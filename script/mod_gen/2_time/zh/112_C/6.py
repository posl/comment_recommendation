def get_input():
    N, T = map(int, input().split())
    c_list = []
    t_list = []
    for i in range(N):
        c, t = map(int, input().split())
        c_list.append(c)
        t_list.append(t)
    return N, T, c_list, t_list

if __name__ == '__main__':
    get_input()