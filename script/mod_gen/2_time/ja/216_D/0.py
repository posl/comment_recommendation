def main():
    N, M = map(int, input().split())
    k = [0] * M
    A = [0] * M
    for i in range(M):
        k[i] = int(input())
        A[i] = list(map(int, input().split()))
    #print(N, M)
    #print(k)
    #print(A)
    for i in range(M):
        #print(A[i])
        for j in range(k[i]):
            #print(A[i][j])
            if A[i][j] == 0:
                continue
            for l in range(M):
                if i == l:
                    continue
                for m in range(k[l]):
                    if A[i][j] == A[l][m]:
                        A[i][j] = 0
                        A[l][m] = 0
                        break
    #print(A)
    for i in range(M):
        for j in range(k[i]):
            if A[i][j] != 0:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()