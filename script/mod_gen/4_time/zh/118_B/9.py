def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(N):
        K.append(list(map(int, input().split())))
        A.append(list(map(int, input().split())))
    #print(N, M, K, A)
    #print(K[0][0])
    #print(A[0][0])
    count = 0
    for i in range(1, M+1):
        for j in range(N):
            if i in A[j]:
                #print(i)
                if j == N-1:
                    count += 1
                    #print(count)
            else:
                break
    print(count)

if __name__ == '__main__':
    main()