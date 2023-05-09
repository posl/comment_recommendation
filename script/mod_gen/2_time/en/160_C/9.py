def main():
    # input
    K, N = map(int, input().split())
    As = list(map(int, input().split()))
    # compute
    # 1. compute the distance between the houses
    dists = [0] * N
    for i in range(N-1):
        dists[i] = As[i+1] - As[i]
    dists[N-1] = K - As[N-1] + As[0]
    # 2. compute the maximum distance
    max_dist = max(dists)
    # output
    print(K - max_dist)

if __name__ == '__main__':
    main()