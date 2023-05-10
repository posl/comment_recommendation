def main():
    # Get input here
    N, K, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    # Calculate the result
    result = 0
    for i in range(N - 1):
        result += A[i]
    if result >= M * N:
        result = 0
    elif M * N - result > K:
        result = -1
    else:
        result = M * N - result
    # Print the result
    print(result)
