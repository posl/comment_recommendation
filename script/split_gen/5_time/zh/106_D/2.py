def main():
    N, M, Q = map(int, input().split())
    train = []
    for i in range(M):
        train.append(list(map(int, input().split())))
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    for i in range(Q):
        temp = 0
        for j in range(M):
            if query[i][0] <= train[j][0] <= train[j][1] <= query[i][1]:
                temp += 1
        print(temp)
