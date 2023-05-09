def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_dist = 0
    for i in range(N):
        if i == N-1:
            dist = K - A[i] + A[0]
        else:
            dist = A[i+1] - A[i]
        if dist > max_dist:
            max_dist = dist
    print(K - max_dist)

if __name__ == '__main__':
    main()