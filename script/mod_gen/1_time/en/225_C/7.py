def main():
    # Read input
    input = sys.stdin.readline
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    # Check whether B is some (unrotated) rectangular part of A
    #   A: 10^100 x 7 matrix
    #   B: N x M matrix
    ans = "No"
    for i in range(10**100 - N + 1):
        for j in range(7 - M + 1):
            if B[0][0] == i * 7 + j + 1:
                if all(B[n][m] == (i + n) * 7 + j + m + 1 for n in range(N) for m in range(M)):
                    ans = "Yes"
                    break
    print(ans)

if __name__ == '__main__':
    main()