def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * N
    for i in range(K):
        B[A[i]-1] = i+1
    for i in range(Q):
        if L[i] == 1:
            if B[0] != 0:
                if B[1] == 0:
                    B[0], B[1] = B[1], B[0]
        else:
            for j in range(N-1):
                if B[j] == L[i]:
                    if B[j+1] == 0:
                        B[j], B[j+1] = B[j+1], B[j]
    for i in range(K):
        print(B.index(i+1)+1, end=" ")

if __name__ == '__main__':
    main()