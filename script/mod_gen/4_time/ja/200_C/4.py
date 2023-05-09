def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = [0] * 200
    for i in range(N):
        cnt[A[i] % 200] += 1
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()