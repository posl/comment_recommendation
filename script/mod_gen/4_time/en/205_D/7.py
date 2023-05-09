def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A.append(10**18)
    for k in K:
        ok = 0
        ng = 10**18
        while ng - ok > 1:
            mid = (ok + ng) // 2
            cnt = 0
            for i in range(N+1):
                cnt += (mid - 1) // A[i]
            if cnt < k:
                ok = mid
            else:
                ng = mid
        print(ok)

if __name__ == '__main__':
    main()