def main():
    N, M, X = [int(i) for i in input().split()]
    A = []
    for i in range(N):
        A.append([int(i) for i in input().split()])
    min_cost = -1
    for i in range(2**N):
        cost = 0
        understanding = [0 for _ in range(M)]
        for j in range(N):
            if i & 2**j:
                cost += A[j][0]
                for k in range(M):
                    understanding[k] += A[j][k+1]
        if min_cost == -1 or (min_cost > cost and min(understanding) >= X):
            min_cost = cost
    print(min_cost)
