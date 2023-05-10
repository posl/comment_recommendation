def main():
    N,M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i],B[i] = map(int, input().split())
    print(N*(N-1)//2 - M)

if __name__ == '__main__':
    main()