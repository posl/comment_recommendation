def main():
    X = input()
    M = int(input())
    d = max([int(x) for x in X])
    if len(X) == 1:
        if d > M:
            print(0)
        else:
            print(1)
        return
    left = d
    right = M + 1
    while right - left > 1:
        mid = (left + right) // 2
        tmp = 0
        for i in range(len(X)):
            tmp = tmp * mid + int(X[i])
            if tmp > M:
                break
        if tmp > M:
            right = mid
        else:
            left = mid
    print(left - d)
