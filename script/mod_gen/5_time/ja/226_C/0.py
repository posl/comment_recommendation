def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
    ans = 0
    for i in range(N-1, -1, -1):
        if K[i] == 0:
            ans = max(ans, T[i])
        else:
            K[i] -= 1
            T[i] += T[A[i][0]-1]
            for j in range(1, len(A[i])):
                K[A[i][j]-1] -= 1
    print(ans)

if __name__ == '__main__':
    main()