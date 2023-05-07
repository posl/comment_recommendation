def main():
    N = int(input())
    W = list(map(int, input().split()))
    if N == 2:
        print(abs(W[0] - W[1]))
        return
    sumW = sum(W)
    minDif = 1000000000000000000
    for i in range(1, N):
        sumW1 = sum(W[:i])
        sumW2 = sumW - sumW1
        minDif = min(minDif, abs(sumW1 - sumW2))
    print(minDif)
