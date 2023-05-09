def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    days = [0] * (10 ** 9 + 1)
    for i in range(N):
        days[A[i]] += 1
        days[A[i] + B[i]] -= 1
    for i in range(1, 10 ** 9 + 1):
        days[i] += days[i - 1]
    ans = [0] * (N + 1)
    for i in range(1, 10 ** 9 + 1):
        ans[days[i]] += 1
    print(*ans[1:])

if __name__ == '__main__':
    main()