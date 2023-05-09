def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #print(N, K, A, X, Y)
    # 0 から 10^10 までの値を2分探索で求める
    ok = 0
    ng = 10 ** 10
    for _ in range(100):
        mid = (ok + ng) / 2
        #print(ok, ng, mid)
        if is_ok(X, Y, A, mid):
            ng = mid
        else:
            ok = mid
    print(ng)

if __name__ == '__main__':
    main()