def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A = A + [A[0] + K]
    dist = []
    for i in range(N):
        dist.append(A[i + 1] - A[i])
    print(K - max(dist))

if __name__ == '__main__':
    main()