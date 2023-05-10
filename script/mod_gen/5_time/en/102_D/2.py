def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    S = [0] * (N + 2)
    for i in range(N + 1):
        S[i + 1] = S[i] + abs(A[i] - A[i + 1])
    def cost(i, j):
        return S[j] - S[i]
    def solve():
        left = 0
        right = 3
        while right < N:
            if cost(left, left + 2) < cost(right - 2, right):
                left += 1
            else:
                right += 1
        ans = 10 ** 18
        for i in range(left, right):
            for j in range(i + 1, right + 1):
                ans = min(ans, max(cost(left, i), cost(i, j), cost(j, right)))
        return ans
    print(solve())
main()

if __name__ == '__main__':
    main()