def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    minA = 100
    for i in range(H):
        for j in range(W):
            if minA > A[i][j]:
                minA = A[i][j]
    result = 0
    for i in range(H):
        for j in range(W):
            result += A[i][j] - minA
    print(result)

if __name__ == '__main__':
    main()