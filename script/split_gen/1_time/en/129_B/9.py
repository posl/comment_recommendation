def main():
    # Read input
    N = int(input())
    W = [int(x) for x in input().split()]
    # Find the minimum possible absolute difference of S_1 and S_2
    ans = sum(W)
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
    # Output the answer
    print(ans)
