def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = []
    for i in range(Q):
        K.append(int(input()))
    # 各要素の差分を求める
    diff = []
    for i in range(N - 1):
        diff.append(A[i + 1] - A[i])
    # print(diff)
    # diff の累積和を求める
    cumsum = [diff[0]]
    for i in range(1, N - 1):
        cumsum.append(cumsum[i - 1] + diff[i])
    # print(cumsum)
    # 累積和の最大公約数を求める
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    ans = []
    for i in range(Q):
        # print("K[i] = ", K[i])
        # print("cumsum = ", cumsum)
        # print("A = ", A)
        # print("N = ", N)
        # print("A[N - 1] = ", A[N - 1])
        # print("A[N - 2] = ", A[N - 2])
        # print("cumsum[N - 2] = ", cumsum[N - 2])
        # print("cumsum[N - 3] = ", cumsum[N - 3])
        if K[i] <= A[0]:
            ans.append(K[i])
        elif K[i] > A[N - 1] - A[N - 2]:
            ans.append(A[N - 1] + K[i] - (A[N - 1] - A[N - 2]))
        else:
            left = 0
            right = N - 2
            while right - left > 1:
                mid = (right + left) // 2
                if K[i] <= cumsum[mid]:
                    right = mid
                else:
                    left = mid
            # print("left = ", left)
            # print("right = ", right)
            # print("cumsum[right] = ", cumsum[right])
            # print("cumsum[left] = ", cumsum[left])
            # print("A
