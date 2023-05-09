def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [0]
    # A[i] <= A[j] となる組み合わせの個数を求める
    def count(i, j):
        if A[i] * A[j] >= 0:
            return (j - i) * (j - i - 1) // 2
        else:
            left = 0
            right = j
            while right - left > 1:
                mid = (left + right) // 2
                if A[mid] * A[j] < 0:
                    left = mid
                else:
                    right = mid
            return (j - i) * (j - right) - (j - right) * (j - right - 1) // 2
    # 二分探索
    left = -10 ** 18
    right = 10 ** 18
    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        for i in range(N + 1):
            if A[i] * A[i] > mid:
                continue
            left = 0
            right = N + 1
            while right - left > 1:
                j = (left + right) // 2
                if A[i] * A[j] <= mid:
                    left = j
                else:
                    right = j
            cnt += count(i, left)
        if cnt >= K:
            right = mid
        else:
            left = mid
    print(right)
