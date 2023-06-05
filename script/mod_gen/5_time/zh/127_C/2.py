def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    print(min(R[0] - L[M - 1] + 1, N - M))

if __name__ == '__main__':
    main()