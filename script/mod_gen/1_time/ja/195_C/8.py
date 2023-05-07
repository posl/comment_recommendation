def main():
    N = int(input())
    ans = 0
    i = 1
    while N >= 1000:
        ans += N % 1000
        N //= 1000
        ans += 1
        i += 1
    ans += N
    print(ans)

if __name__ == '__main__':
    main()