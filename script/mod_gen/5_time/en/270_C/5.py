def read_ints():
    return list(map(int, input().split()))
N, X, Y = read_ints()
edges = []
for i in range(N-1):
    edges.append(read_ints())

if __name__ == '__main__':
    read_ints()