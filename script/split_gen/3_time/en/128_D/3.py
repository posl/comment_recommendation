def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_sum = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            jewels = V[:i] + V[N - j:]
            jewels.sort()
            sum_jewels = sum(jewels)
            for k in range(min(K - i - j, i + j)):
                if jewels[k] < 0:
                    sum_jewels -= jewels[k]
            if sum_jewels > max_sum:
                max_sum = sum_jewels
    print(max_sum)
