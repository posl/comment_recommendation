def main():
    X = input()
    M = int(input())
    d = int(max(list(X)))
    X = list(X)
    X.reverse()
    X = [int(x) for x in X]
    if len(X) == 1:
        if X[0] <= M:
            print(1)
        else:
            print(0)
        return
    def convert(n):
        if n == 0:
            return 0
        base = d + 1
        result = 0
        for i in range(len(X)):
            result += X[i] * (base ** i)
        return result
    # 二分法
    left = d + 1
    right = M + 1
    while left < right:
        mid = (left + right) // 2
        if convert(mid) <= M:
            left = mid + 1
        else:
            right = mid
    print(left - d - 1)
