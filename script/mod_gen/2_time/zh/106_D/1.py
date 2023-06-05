def get_input():
    n, m, q = map(int, input().split())
    lr = []
    pq = []
    for i in range(m):
        lr.append(list(map(int, input().split())))
    for i in range(q):
        pq.append(list(map(int, input().split())))
    return n, m, q, lr, pq

if __name__ == '__main__':
    get_input()