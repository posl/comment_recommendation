def main():
    # Read in the input
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(N)]
    # Check if B is a submatrix of A
    if B[0][0] % 7 == 1 and B[0][0] + 7 * (N - 1) + M - 1 <= 10 ** 100 * 7:
        print("Yes")
    else:
        print("No")
main()
