def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [abs(a) for a in A]
    A.sort(reverse=True)
    minus = 0
    plus = 0
    zero = 0
    for a in A:
        if a < 0:
            minus += 1
        elif a > 0:
            plus += 1
        else:
            zero += 1
    if zero > 0:
        if K <= minus * plus + zero * (zero - 1) // 2:
            print(0)
            return
        else:
            K -= minus * plus + zero * (zero - 1) // 2
    if K <= minus * (minus - 1) // 2:
        left = -1
        right = N
        while right - left > 1:
            mid = (left + right) // 2
            if A[mid] * A[mid + 1] <= 0:
                right = mid
            else:
                left = mid
        print(A[right] * A[right - K + 1])
        return
    else:
        K -= minus * (minus - 1) // 2
    left = -1
    right = N
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] * A[mid - 1] <= 0:
            left = mid
        else:
            right = mid
    print(A[left] * A[left - K + 1])
    return
