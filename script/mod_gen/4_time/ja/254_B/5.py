def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([1]*(i+1))
        for j in range(1,i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]
    for i in range(N):
        print(*A[i])

if __name__ == '__main__':
    main()