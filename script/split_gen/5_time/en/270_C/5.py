def read_ints():
    return list(map(int, input().split()))
N, X, Y = read_ints()
edges = []
for i in range(N-1):
    edges.append(read_ints())
