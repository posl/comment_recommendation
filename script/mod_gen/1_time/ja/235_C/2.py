def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    for i in range(Q):
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if A[mid] == X[i]:
                if K[i] == 1:
                    right = mid
                else:
                    K[i] -= 1
                    left = mid + 1
            elif A[mid] < X[i]:
                left = mid + 1
            else:
                right = mid
        if left == N or A[left] != X[i]:
            print(-1)
        else:
            print(left + 1)

if __name__ == '__main__':
    main()