def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_value = 0
    for left in range(min(N, K) + 1):
        for right in range(min(N, K) + 1 - left):
            values = V[:left] + V[N - right:]
            values.sort()
            for i in range(min(K - left - right, len(values))):
                if values[i] < 0:
                    values[i] = 0
            max_value = max(max_value, sum(values))
    print(max_value)
