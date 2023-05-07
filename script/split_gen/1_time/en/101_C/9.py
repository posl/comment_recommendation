def main():
    # Get inputs
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # Initialize variables
    cnt = 0
    # Find the minimum number of operations required
    if (N - K) % (K - 1) == 0:
        cnt = (N - K) // (K - 1) + 1
    else:
        cnt = (N - K) // (K - 1) + 2
    # Print the minimum number of operations required
    print(cnt)
