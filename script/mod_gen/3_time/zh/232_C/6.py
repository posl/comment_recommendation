def main():
    N,M = map(int,input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c,d = map(int,input().split())
        C.append(c)
        D.append(d)
    #print(A,B,C,D)
    #print(N,M)
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i != j:
                for k in range(M):
                    if A[k] == i and B[k] == j:
                        for l in range(M):
                            if C[l] == i and D[l] == j:
                                break
                        else:
                            break
                else:
                    for l in range(M):
                        if C[l] == i and D[l] == j:
                            break
                    else:
                        print("No")
                        break
            if i == N and j == N:
                print("Yes")

if __name__ == '__main__':
    main()