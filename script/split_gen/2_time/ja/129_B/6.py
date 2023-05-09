def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000
    for i in range(1, N):
        sum1 = sum(W[:i])
        sum2 = sum(W[i:])
        diff = abs(sum1 - sum2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
