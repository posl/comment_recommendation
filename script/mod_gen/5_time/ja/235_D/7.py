def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n = n // a
            ans += 1
        elif n % 10 == 1:
            n = n // 10
            ans += 1
        else:
            ans = -1
            break
    print(ans)

if __name__ == '__main__':
    main()