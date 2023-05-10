def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()