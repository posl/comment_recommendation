def main():
    N = int(input())
    S = input().split()
    A = [0 for i in range(N)]
    for i in range(N):
        A[i] = int(S[i])
    for i in range(N):
        print(A[i], end=' ')
        for j in range(i+1, N):
            A[j] = A[j-1] + A[j] - A[i]
        print()

if __name__ == '__main__':
    main()