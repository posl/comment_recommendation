def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(30, -1, -1):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:
                cnt += 1
        if cnt >= 2:
            ans += 1 << i
            for j in range(n):
                if a[j] >> i & 1:
                    a[j] -= 1 << i
    print(ans)
    return

if __name__ == '__main__':
    main()