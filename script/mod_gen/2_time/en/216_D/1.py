def main():
    N, M = map(int, input().split())
    K = [0] * M
    A = [0] * M
    for i in range(M):
        K[i] = int(input())
        A[i] = list(map(int, input().split()))
    #print(N, M)
    #print(K)
    #print(A)
    count = [0] * (N + 1)
    for i in range(M):
        for j in range(K[i]):
            count[A[i][j]] += 1
    #print(count)
    for i in range(1, N + 1):
        if count[i] % 2 != 0:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()