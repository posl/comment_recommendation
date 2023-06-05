def main():
    N = int(input())
    A = list(map(int, input().split()))
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        left[i + 1] = left[i] + A[i]
        right[i + 1] = right[i] + A[N - 1 - i]
    left_max = [0] * (N + 1)
    right_max = [0] * (N + 1)
    for i in range(N):
        left_max[i + 1] = max(left_max[i], left[i + 1])
        right_max[i + 1] = max(right_max[i], right[i + 1])
    ans = 10 ** 18
    for i in range(N + 1):
        ans = min(ans, max(left_max[i], right_max[N - i]) - min(left[i], right[N - i]))
    print(ans)

if __name__ == '__main__':
    main()