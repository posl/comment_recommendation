def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        n = N // i
        ans += n * (n+1) // 2 * i
    print(ans)

if __name__ == '__main__':
    main()