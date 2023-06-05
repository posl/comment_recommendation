def main():
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    if N >= M:
        print(0)
        return
    else:
        dist = sorted([X[i+1] - X[i] for i in range(M-1)])
        print(sum(dist[:M-N]))
main()
