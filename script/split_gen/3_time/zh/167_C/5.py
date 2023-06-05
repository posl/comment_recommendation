def main():
    N, M, X = map(int, input().split())
    books = []
    for i in range(N):
        books.append(list(map(int, input().split())))
    min_cost = 1000000
    for i in range(2**N):
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += books[j][0]
                for k in range(M):
                    understand[k] += books[j][k+1]
        if min(understand) >= X and cost < min_cost:
            min_cost = cost
    if min_cost == 1000000:
        print(-1)
    else:
        print(min_cost)
