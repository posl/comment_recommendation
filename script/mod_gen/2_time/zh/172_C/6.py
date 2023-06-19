def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 读取A的书需要的时间
    A_time = [0]
    for a in A:
        A_time.append(A_time[-1] + a)
    # 读取B的书需要的时间
    B_time = [0]
    for b in B:
        B_time.append(B_time[-1] + b)
    # 二分查找
    ans = 0
    for i in range(N + 1):
        if A_time[i] > K:
            break
        # 二分查找
        ok = M + 1
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if A_time[i] + B_time[mid] <= K:
                ng = mid
            else:
                ok = mid
        ans = max(ans, i + ng)
    print(ans)

if __name__ == '__main__':
    main()