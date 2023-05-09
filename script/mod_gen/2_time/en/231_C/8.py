def main():
    #input
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    x = [int(input()) for _ in range(Q)]
    #sort
    A.sort()
    #cumulative sum
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    #binary search
    for i in range(Q):
        ok = 0
        ng = N+1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A[mid-1] >= x[i]:
                ng = mid
            else:
                ok = mid
        print(N-ng+1)

if __name__ == '__main__':
    main()