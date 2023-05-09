def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    #print(K, N)
    #print(A)
    max_dist = 0
    for i in range(N-1):
        max_dist = max(max_dist, A[i+1] - A[i])
    max_dist = max(max_dist, K - A[N-1] + A[0])
    #print(max_dist)
    print(K - max_dist)

if __name__ == '__main__':
    main()