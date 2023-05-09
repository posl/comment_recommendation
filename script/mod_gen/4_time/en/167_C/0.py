def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    
    min_cost = float('inf')
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i & (1 << j):
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        
        if min(understanding) >= X:
            min_cost = min(min_cost, cost)
    
    if min_cost == float('inf'):
        print(-1)
    else:
        print(min_cost)

if __name__ == '__main__':
    main()