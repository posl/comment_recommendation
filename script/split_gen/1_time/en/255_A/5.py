def main():
    # Get input
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    # Output
    print(A[R-1][C-1])
