def main():
    H, W, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    A = list(set(A))
    B = list(set(B))
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    for i in range(N):
        print(A.index(A[i]) + 1, B.index(B[i]) + 1)

if __name__ == '__main__':
    main()