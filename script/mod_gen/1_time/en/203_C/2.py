def main():
    N, K = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.append(0)
    B.append(0)
    A.append(10 ** 100 + 1)
    B.append(0)
    A, B = (list(t) for t in zip(*sorted(zip(A, B))))
    #print(A)
    #print(B)
    for i in range(N + 1):
        if A[i] <= K + 1:
            K += B[i]
        else:
            break
    print(K + 1)

if __name__ == '__main__':
    main()