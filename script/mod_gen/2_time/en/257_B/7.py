def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * (N + 2)
    for a in A:
        B[a] = 1
    for l in L:
        if B[A[l - 1] + 1] == 1:
            continue
        else:
            B[A[l - 1]] -= 1
            B[A[l - 1] + 1] += 1
            A[l - 1] += 1
    for i in range(1, N + 1):
        print(B[i], end=' ')

if __name__ == '__main__':
    main()