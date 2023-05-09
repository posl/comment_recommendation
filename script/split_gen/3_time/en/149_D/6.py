def main():
    # Read input
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # Initialize
    score = 0
    prev = [None]*K
    # Play
    for i in range(N):
        # Get score
        if T[i] == "r":
            score += P
            prev[i%K] = "p"
        elif T[i] == "s":
            score += R
            prev[i%K] = "r"
        elif T[i] == "p":
            score += S
            prev[i%K] = "s"
        # Check previous hand
        if i >= K and prev[i%K] == prev[(i-K)%K]:
            score -= R if prev[i%K] == "r" else (S if prev[i%K] == "s" else P)
            prev[i%K] = None
    # Output
    print(score)
