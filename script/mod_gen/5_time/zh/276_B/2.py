def get_data():
    N, M = input().split()
    N = int(N)
    M = int(M)
    data = []
    for i in range(M):
        a, b = input().split()
        a = int(a)
        b = int(b)
        data.append([a, b])
    return N, M, data

if __name__ == '__main__':
    get_data()