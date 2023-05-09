def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    left = 0
    right = 0
    while left < N:
        while right < N:
            total += A[right]
            if total >= K:
                break
            right += 1
        if total < K:
            break
        if total == K:
            print("left: {}, right: {}".format(left, right))
        total -= A[left]
        left += 1
        right += 1
    print("total: {}".format(total))
