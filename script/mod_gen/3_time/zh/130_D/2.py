def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = 0
    ans = 0
    right = 0
    for left in range(N):
        while right < N and s + A[right] < K:
            s += A[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            s -= A[left]
    print(ans)

if __name__ == '__main__':
    main()