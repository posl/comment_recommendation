def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] += 1
    ans = 0
    for i in range(N):
        if B[i + 1] == 0:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()