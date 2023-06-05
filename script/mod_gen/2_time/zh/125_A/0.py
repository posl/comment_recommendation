def main():
    n, k = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += 1
        else:
            if k > 0:
                k -= 1
                ans += 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()