def main():
    N = int(input())
    W = list(map(int, input().split()))
    W_sum = sum(W)
    W_sum1 = 0
    W_sum2 = 0
    for i in range(N):
        W_sum1 += W[i]
        W_sum2 = W_sum - W_sum1
        if i == 0:
            min_diff = abs(W_sum1 - W_sum2)
        elif abs(W_sum1 - W_sum2) < min_diff:
            min_diff = abs(W_sum1 - W_sum2)
    print(min_diff)
