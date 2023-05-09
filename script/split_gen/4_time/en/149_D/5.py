def main():
    # Get input here
    N, K = map(int, input().strip().split())
    R, S, P = map(int, input().strip().split())
    T = input().strip()
    # Calculate result here
    result = get_max_score(N, K, R, S, P, T)
    # Print output here
    print(result)
