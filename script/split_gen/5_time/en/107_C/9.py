def main():
    # Get the input
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    # Find the minimum time required to light K candles
    min_time = min(abs(x[i]) * 2 + abs(x[i] - x[i + k - 1]) for i in range(n - k + 1))
    # Print the minimum time required to light K candles
    print(min_time)
