def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append([0 for j in range(i+1)])
        for j in range(i+1):
            if j == 0 or j == i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]
        print(' '.join(map(str, A[i])))

if __name__ == '__main__':
    main()