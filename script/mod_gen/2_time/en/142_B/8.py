def main():
    #N: number of friends
    #K: height limit
    N, K = map(int, input().split())
    #h_i: height of i-th friend
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

if __name__ == '__main__':
    main()