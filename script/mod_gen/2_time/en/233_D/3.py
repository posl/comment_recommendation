def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(i, N):
            tmp += A[j]
            if tmp == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()