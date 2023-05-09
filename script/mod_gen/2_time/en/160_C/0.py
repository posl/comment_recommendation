def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    dist = []
    for i in range(N-1):
        dist.append(A[i+1] - A[i])
    dist.append(K + A[0] - A[N-1])
    print(K - max(dist))

if __name__ == '__main__':
    main()