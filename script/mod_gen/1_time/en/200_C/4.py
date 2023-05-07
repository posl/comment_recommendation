def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    cnt = [0] * mod
    for a in A:
        cnt[a % mod] += 1
    ans = 0
    for c in cnt:
        if c > 1:
            ans += c * (c - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()