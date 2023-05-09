def main():
    A, B, X = map(int, input().split())
    if A * 10**9 + B * 10 <= X:
        print(10**9)
        return
    left = 0
    right = 10**9
    while right - left > 1:
        mid = (left + right) // 2
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid
    print(left)
