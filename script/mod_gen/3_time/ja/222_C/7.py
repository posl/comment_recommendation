def main():
    N, M = map(int, input().split())
    A = []
    for i in range(2*N):
        A.append(input())
    #print(A)
    #print(N, M)
    rank = [i+1 for i in range(2*N)]
    #print(rank)
    for i in range(M):
        #print("i=", i)
        #print("rank=", rank)
        for k in range(N):
            #print("k=", k)
            p1 = rank[2*k]
            p2 = rank[2*k+1]
            #print("p1=", p1)
            #print("p2=", p2)
            if A[p1-1][i] == A[p2-1][i]:
                continue
            elif A[p1-1][i] == "G" and A[p2-1][i] == "C":
                rank[2*k] = p2
                rank[2*k+1] = p1
            elif A[p1-1][i] == "C" and A[p2-1][i] == "P":
                rank[2*k] = p2
                rank[2*k+1] = p1
            elif A[p1-1][i] == "P" and A[p2-1][i] == "G":
                rank[2*k] = p2
                rank[2*k+1] = p1
    for i in range(2*N):
        print(rank[i])

if __name__ == '__main__':
    main()