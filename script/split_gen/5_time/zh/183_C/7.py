def read_data():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(list(map(int, input().split())))
    return N, K, T
N, K, T = read_data()
