def isSquare(n):
    if n < 0:
        return False
    if n == 1:
        return True
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid * mid == n:
            return True
        if mid * mid < n:
            low = mid + 1
        else:
            high = mid
    return False
