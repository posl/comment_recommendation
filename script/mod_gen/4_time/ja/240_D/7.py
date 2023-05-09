def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = [0] * N
    cnt = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        ans[i] = i + 1 - cnt[a[i]]
        cnt[a[i]] += 1
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()