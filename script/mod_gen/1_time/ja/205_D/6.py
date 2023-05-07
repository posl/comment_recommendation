def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(10**18)
    ans = []
    for k in K:
        if k <= A[0]:
            ans.append(k)
            continue
        left = 0
        right = N
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] - A[mid-1] - 1 < k:
                k -= A[mid] - A[mid-1] - 1
                left = mid
            else:
                right = mid
        ans.append(A[left] + k)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()