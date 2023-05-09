def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [x % 200 for x in a]
    cnt = [0] * 200
    for i in a:
        cnt[i] += 1
    ans = 0
    for i in cnt:
        ans += i * (i - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()