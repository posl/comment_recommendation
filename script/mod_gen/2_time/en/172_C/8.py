def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # create cumulative sums of list A and B
    A_cumsum = [0] + list(accumulate(A))
    B_cumsum = [0] + list(accumulate(B))
    # find the max number of books that can be read in K minutes
    ans = 0
    for i in range(N + 1):
        if A_cumsum[i] > K:
            break
        # binary search for the largest j that satisfies B_cumsum[j] <= K - A_cumsum[i]
        j = bisect.bisect_right(B_cumsum, K - A_cumsum[i])
        ans = max(ans, i + j - 1)
    print(ans)

if __name__ == '__main__':
    main()