def main():
    N = int(input())
    ans = 0
    cnt = 1
    while N > 0:
        ans += N // 1000
        N = N // 1000
    print(ans)

if __name__ == '__main__':
    main()