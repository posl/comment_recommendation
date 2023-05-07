def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    minA = min([min(Ai) for Ai in A])
    maxA = max([max(Ai) for Ai in A])
    minCount = 10000
    for i in range(minA, maxA+1):
        count = 0
        for j in range(H):
            for k in range(W):
                if A[j][k] > i:
                    count += A[j][k] - i
        minCount = min(minCount, count)
    print(minCount)
