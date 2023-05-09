def main():
    N = int(input())
    A = list(map(int, input().split()))
    left = [0] * N
    right = [0] * N
    left[0] = A[0]
    right[-1] = A[-1]
    for i in range(1, N):
        left[i] = left[i - 1] + A[i]
        right[-i - 1] = right[-i] + A[-i - 1]
    left_min = min(left)
    left_max = max(left)
    right_min = min(right)
    right_max = max(right)
    ans = min(left_max - left_min, right_max - right_min)
    for i in range(N - 3):
        ans = min(ans, max(left[i], right[i + 1]) - min(left[i], right[i + 1]))
    print(ans)

if __name__ == '__main__':
    main()