def main():
    # Read data
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # Compute the set of sums
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    # Find the greatest multiple of D in S
    ans = -1
    for x in S:
        if x % D == 0:
            ans = max(ans, x)
    # Print the answer
    print(ans)
main()
