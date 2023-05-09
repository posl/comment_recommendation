def main():
    N = int(input())
    X = list(map(int, input().split()))
    min_cost = 1000000000
    for i in range(1, 101):
        cost = 0
        for j in range(N):
            cost += (X[j] - i) ** 2
        if min_cost > cost:
            min_cost = cost
    print(min_cost)
