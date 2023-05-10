def main():
    # input
    a, N = map(int, input().split())
    # solve
    ans = 0
    while N > 1:
        if N % a == 0:
            N //= a
        elif N % 10 == 1:
            N //= 10
        else:
            print(-1)
            exit()
        ans += 1
    # output
    print(ans)

if __name__ == '__main__':
    main()