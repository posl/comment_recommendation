def get_input_data():
    n, m, q = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    pq = [list(map(int, input().split())) for _ in range(q)]
    return n, m, q, lr, pq

if __name__ == '__main__':
    get_input_data()