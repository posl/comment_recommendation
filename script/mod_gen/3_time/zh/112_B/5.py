def get_input():
    N, T = input().split()
    N = int(N)
    T = int(T)
    if N < 1 or N > 100 or T < 1 or T > 1000:
        return None
    c = []
    t = []
    for i in range(N):
        c_i, t_i = input().split()
        c_i = int(c_i)
        t_i = int(t_i)
        if c_i < 1 or c_i > 1000 or t_i < 1 or t_i > 1000:
            return None
        c.append(c_i)
        t.append(t_i)
    return N, T, c, t

if __name__ == '__main__':
    get_input()