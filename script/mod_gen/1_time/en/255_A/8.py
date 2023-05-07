def main():
    # Read input
    R,C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(2)]
    # Solve problem
    ans = A[R-1][C-1]
    # Print output
    print(ans)

if __name__ == '__main__':
    main()