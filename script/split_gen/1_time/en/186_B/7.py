def main():
    # H,W = map(int, input().split())
    # A = [list(map(int, input().split())) for _ in range(H)]
    H, W = 3, 2
    A = [[4, 4], [4, 4], [4, 4]]
    A = [[99, 99, 99], [99, 0, 99], [99, 99, 99]]
    A = [[2, 2, 3], [3, 2, 2]]
    # print(A)
    # print(H, W)
    minA = min([min(a) for a in A])
    maxA = max([max(a) for a in A])
    # print(minA, maxA)
    minDiff = 10000
    for i in range(minA, maxA + 1):
        diff = 0
        for a in A:
            diff += sum([abs(i - j) for j in a])
        minDiff = min(diff, minDiff)
    print(minDiff)
