def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 360
    for i in range(N):
        B[A[i]] = 1
    for i in range(1, 360):
        B[i] += B[i-1]
    ans = 0
    for i in range(360):
        ans = max(ans, B[i])
        if i >= N:
            ans = max(ans, B[i] - B[i-N])
    print(360 - ans)

if __name__ == '__main__':
    main()