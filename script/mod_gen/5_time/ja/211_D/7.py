def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(A)
    print(B)
    #for i in range(M):
    #    print(A[i], B[i])

if __name__ == '__main__':
    main()