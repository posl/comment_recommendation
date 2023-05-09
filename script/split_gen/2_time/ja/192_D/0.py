def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    left = d
    right = M + 1
    while right - left > 1:
        mid = (left + right) // 2
        value = 0
        for i in range(len(X)):
            value = value * mid + int(X[i])
        if value <= M:
            left = mid
        else:
            right = mid
    print(left - d)
