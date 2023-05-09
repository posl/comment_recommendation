def main():
    # Get the input
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    # Swap the terms
    B = A[:P-1] + A[R-1:S] + A[Q:S-R+P-1] + A[S:]
    # Print the result
    print(' '.join(map(str, B)))
