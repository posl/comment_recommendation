def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Calculate the total score
    total = 0
    for i in range(N-1):
        total += A[i]
    # Calculate the minimum score on the final subject
    min_score = M * N - total
    # If the minimum score is negative or larger than K, the goal can not be achieved
    if min_score < 0 or min_score > K:
        print(-1)
    else:
        print(min_score)
