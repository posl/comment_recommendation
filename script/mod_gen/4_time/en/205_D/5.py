def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    for k in K:
        # 二分探索
        ok = 10**18
        ng = 0
        while ok - ng > 1:
            mid = (ok + ng) // 2
            cnt = 0
            for i in range(N):
                cnt += (mid - 1) // A[i]
            if cnt >= k:
                ok = mid
            else:
                ng = mid
        print(ok)

if __name__ == '__main__':
    main()