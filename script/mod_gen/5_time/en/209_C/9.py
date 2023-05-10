def main():
    # Read from Standard Input
    N = int(input())
    C = list(map(int, input().split()))
    # Solve the problem
    MOD = 10**9+7
    C.sort()
    ans = 1
    for i in range(N):
        ans = ans * max(C[i]-i, 0) % MOD
    # Write the answer to Standard Output
    print(ans)

if __name__ == '__main__':
    main()