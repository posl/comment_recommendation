def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    
    def solve(K):
        if K <= A[0]-1:
            return K
        elif K >= A[-1]+1:
            return K + A[-1]
        
        ng = 0
        ok = N-1
        while ok-ng > 1:
            mid = (ok+ng)//2
            if A[mid] <= K:
                ng = mid
            else:
                ok = mid
        return K + A[ng]
    
    for k in K:
        print(solve(k))

if __name__ == '__main__':
    main()