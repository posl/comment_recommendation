def main():
    N = int(input())
    W = list(map(int, input().split()))
    sumW = sum(W)
    minDiff = sumW
    for i in range(1, N):
        sum1 = sum(W[:i])
        sum2 = sumW - sum1
        diff = abs(sum1 - sum2)
        if diff < minDiff:
            minDiff = diff
    print(minDiff)

if __name__ == '__main__':
    main()