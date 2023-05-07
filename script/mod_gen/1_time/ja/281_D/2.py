def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, D)
    #print(A)
    S = []
    for i in range(N):
        for j in range(i+1, N):
            S.append(A[i]+A[j])
    print(S)

if __name__ == '__main__':
    main()