def get_input():
    n, m, q = map(int, input().split())
    l_r = [list(map(int, input().split())) for _ in range(m)]
    p_q = [list(map(int, input().split())) for _ in range(q)]
    return n, m, q, l_r, p_q

if __name__ == '__main__':
    get_input()