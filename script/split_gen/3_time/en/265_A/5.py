def main():
    X, Y, N = map(int, input().split())
    min_cost = 100 * N
    for i in range(N+1):
        for j in range(N+1):
            if i + j <= N:
                cost = X * i + Y * j
                if cost < min_cost:
                    min_cost = cost
    print(min_cost)
