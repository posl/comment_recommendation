def solve(N, K, P):
    #print(N, K, P)
    #print("P: ", P)
    table = [0] * (N+1)
    for i in range(N):
        table[P[i]] = i+1
    #print("table: ", table)
    for i in range(1, N+1):
        if table[i] > 0:
            table[i] = table[i-1]
    #print("table: ", table)
    for i in range(N):
        if i+1 < K:
            print(-1)
        else:
            print(table[i+1])

if __name__ == '__main__':
    solve()