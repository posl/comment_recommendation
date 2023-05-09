def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for _ in range(Q):
        X.append(int(input()))
    A.sort()
    for x in X:
        # 二分探索
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if A[mid] >= x:
                right = mid
            else:
                left = mid + 1
        print(N - left)

if __name__ == '__main__':
    main()