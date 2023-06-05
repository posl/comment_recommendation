def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if s[i] % 6 == 0:
            continue
        elif s[i] % 6 == 2:
            ans += 1
        elif s[i] % 6 == 4:
            ans += 1
        elif s[i] % 6 == 5:
            ans += 2
    print(ans)

if __name__ == '__main__':
    main()