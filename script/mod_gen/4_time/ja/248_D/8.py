def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(N)
    #print(A)
    #print(Q)
    #print(query)
    for i in range(Q):
        L = query[i][0]
        R = query[i][1]
        X = query[i][2]
        #print(L, R, X)
        #print(A[L-1:R].count(X))
        print(A[L-1:R].count(X))
main()

if __name__ == '__main__':
    main()