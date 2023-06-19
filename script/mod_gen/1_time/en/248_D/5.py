def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    #print(N, A, Q, queries)
    
    # 1. count the number of each number
    count = [0] * (N+1)
    for a in A:
        count[a] += 1
    
    # 2. accumulative sum
    accum = [0] * (N+1)
    for i in range(1, N+1):
        accum[i] = accum[i-1] + count[i]
    
    # 3. answer queries
    for l, r, x in queries:
        print(accum[r] - accum[l-1])
solve()
