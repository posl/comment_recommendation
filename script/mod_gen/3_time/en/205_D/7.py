def main():
    #input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #compute
    #B[i] := A[i] - A[i-1] - 1
    B = [A[0]-1] + [A[i]-A[i-1]-1 for i in range(1, N)]
    #C[i] := B[0] + B[1] + ... + B[i]
    C = [B[0]] + [C[i-1]+B[i] for i in range(1, N)]
    #D[i] := D[i-1] + C[i-1] + 1
    D = [0] + [D[i-1]+C[i-1]+1 for i in range(1, N)]
    #output
    for k in K:
        #binary search
        #A[i] - D[i] <= k <= A[i+1] - D[i+1]
        left, right = 0, N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] - D[mid] <= k:
                left = mid
            else:
                right = mid
        print(k + D[left])

if __name__ == '__main__':
    main()