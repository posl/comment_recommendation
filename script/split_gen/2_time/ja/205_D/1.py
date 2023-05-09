def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    for k in K:
        left = 1
        right = 10**18
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for a in A:
                count += mid // a
            if count >= k:
                right = mid - 1
            else:
                left = mid + 1
        print(left)
