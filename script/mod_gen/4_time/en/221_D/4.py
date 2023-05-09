def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    days = [0] * (10**9 + 2)
    for i in range(N):
        days[A[i]] += 1
        days[A[i] + B[i]] -= 1
    for i in range(1, 10**9 + 2):
        days[i] += days[i - 1]
    ans = [0] * N
    for i in range(N):
        ans[days[A[i]] - 1] += 1
    print(*ans)

if __name__ == '__main__':
    main()