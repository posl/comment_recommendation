def main():
    # Get input here
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    # Calculate result here
    min_diff = float('inf')
    min_index = 0
    for i in range(N):
        diff = abs(T - H[i] * 0.006 - A)
        if diff < min_diff:
            min_diff = diff
            min_index = i + 1
    # Print result here
    print(min_index)
