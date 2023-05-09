def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (10**6+1)
    for i in range(N):
        ans += cnt[A[i]]
        cnt[A[i]] += 1
    print(ans)

if __name__ == '__main__':
    main()