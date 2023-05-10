def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    dist = [0]*(M-1)
    for i in range(M-1):
        dist[i] = X[i+1]-X[i]
    dist.sort()
    print(sum(dist[:max(M-N, 0)]))

if __name__ == '__main__':
    main()