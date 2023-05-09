def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for i in a:
        cnt[i] += 1
    ans = 0
    for i in cnt:
        ans += i * (i - 1) // 2
    for i in a:
        print(ans - cnt[i] + 1)

if __name__ == '__main__':
    main()