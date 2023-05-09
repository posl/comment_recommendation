def main():
    X = input()
    M = int(input())
    lenX = len(X)
    d = int(max(X))
    if lenX == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    left = d
    right = M+1
    while left + 1 < right:
        mid = (left + right) // 2
        if check(X, M, mid):
            left = mid
        else:
            right = mid
    print(left-d)
