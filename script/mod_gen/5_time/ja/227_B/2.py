def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] == 1:
            ans += 1
            continue
        for j in range(2, s[i]):
            if s[i] % j == 0:
                ans += 1
                break
    print(n - ans)

if __name__ == '__main__':
    main()