def solve(N, K, A):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # Return the number of operations
    if K == 2:
        return N - 1
    else:
        return N - 2

if __name__ == '__main__':
    solve()