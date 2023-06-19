def read_data():
    line1 = input().split()
    N = int(line1[0])
    M = int(line1[1])
    Q = int(line1[2])
    trains = []
    for i in range(M):
        line = input().split()
        trains.append((int(line[0]), int(line[1])))
    queries = []
    for i in range(Q):
        line = input().split()
        queries.append((int(line[0]), int(line[1])))
    return N, M, Q, trains, queries
