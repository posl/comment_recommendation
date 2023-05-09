def main():
    N, M = [int(x) for x in input().split()]
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = [int(x) for x in input().split()]
    K = int(input())
    C = [0] * K
    D = [0] * K
    for i in range(K):
        C[i], D[i] = [int(x) for x in input().split()]
    ans = 0
    for i in range(2 ** K):
        dish = [0] * N
        for j in range(K):
            if (i >> j) & 1 == 0:
                dish[C[j] - 1] += 1
            else:
                dish[D[j] - 1] += 1
        satisfied = 0
        for j in range(M):
            if dish[A[j] - 1] > 0 and dish[B[j] - 1] > 0:
                satisfied += 1
        ans = max(ans, satisfied)
    print(ans)

if __name__ == '__main__':
    main()