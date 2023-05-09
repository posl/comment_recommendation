def main():
    N, M, X = map(int, input().split())
    books = []
    for i in range(N):
        books.append(list(map(int, input().split())))
    min_cost = -1
    for i in range(2**N):
        cost = 0
        algos = [0]*M
        for j in range(N):
            if i >> j & 1:
                cost += books[j][0]
                for k in range(M):
                    algos[k] += books[j][k+1]
        if min_cost == -1:
            if min(algos) >= X:
                min_cost = cost
        else:
            if min(algos) >= X:
                min_cost = min(min_cost, cost)
    print(min_cost)
