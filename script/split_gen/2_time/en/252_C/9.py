def main():
    # Take input
    N = int(input())
    S = [input() for _ in range(N)]
    # Initialize variables
    ans = 0
    # Compute the answer
    for i in range(10):
        # Initialize variables
        count = 0
        # Compute the answer
        for j in range(N):
            count += min((int(S[j][i]) - int(S[j][0])) % 10, (int(S[j][0]) - int(S[j][i])) % 10)
        # Update the answer
        ans = max(ans, count)
    # Output the answer
    print(ans)
