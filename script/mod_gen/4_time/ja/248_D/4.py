def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    queries = []
    for i in range(Q):
        queries.append([int(x) for x in input().split()])
    
    #print(N)
    #print(A)
    #print(Q)
    #print(queries)
    
    for i in range(Q):
        L = queries[i][0]
        R = queries[i][1]
        X = queries[i][2]
        count = 0
        for j in range(L-1, R):
            if A[j] == X:
                count += 1
        print(count)

if __name__ == '__main__':
    main()