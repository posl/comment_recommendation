def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(len(A))
    #print(len(B))
    for i in range(M):
        if A[i] == 1:
            for j in range(M):
                if B[i] == A[j]:
                    if B[j] == N:
                        print("Yes")
                        return
    print("No")
    return

if __name__ == '__main__':
    main()