def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    result = 0
    for l in range(min(K, N)+1):
        for r in range(min(K, N)-l+1):
            if l+r > N:
                continue
            if l+r > K:
                continue
            tmp = V[:l] + V[N-r:]
            tmp.sort()
            result = max(result, sum(tmp[K-l-r:]))
    print(result)

if __name__ == '__main__':
    main()