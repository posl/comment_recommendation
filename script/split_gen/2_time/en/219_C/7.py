def main():
    # Input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # Solve
    S = sorted(S, key=lambda s: [X.index(c) for c in s])
    # Output
    for s in S:
        print(s)
