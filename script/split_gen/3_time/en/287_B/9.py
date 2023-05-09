def main():
    # Read input data
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # Count the number of strings among S whose last three characters coincide with one or more of T
    count = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                count += 1
                break
    # Print the answer
    print(count)
