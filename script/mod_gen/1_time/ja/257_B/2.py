def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * (N + 1)
    for a in A:
        B[a] = 1
    for l in L:
        if B[l] == 1 and l < N:
            B[l] = 0
            B[l + 1] = 1
    for i in range(1, N + 1):
        if B[i] == 1:
            print(i, end=' ')

if __name__ == '__main__':
    main()