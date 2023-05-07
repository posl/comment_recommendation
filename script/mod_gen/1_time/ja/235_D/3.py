def main():
    a, N = map(int, input().split())
    ans = 0
    while N > 1:
        if N % a == 0:
            N //= a
        else:
            if N % 10 == 0:
                N //= 10
            else:
                print(-1)
                return
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()