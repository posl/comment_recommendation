def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += N // i
    print(ans)

if __name__ == '__main__':
    main()