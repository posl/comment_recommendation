def main():
    # Input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Solve
    if sum(A) > N:
        ans = -1
    else:
        ans = N - sum(A)
    # Output
    print(ans)

if __name__ == '__main__':
    main()