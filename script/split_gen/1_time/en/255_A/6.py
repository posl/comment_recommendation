def main():
    # read the input
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]
    # print the output
    print(A[R-1][C-1])
