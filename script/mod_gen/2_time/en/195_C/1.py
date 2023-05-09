def main():
    N = int(input())
    ans = 0
    i = 0
    while N > 0:
        ans += (N + 8) // 1000 * i
        N //= 1000
        i += 1
    print(ans)

if __name__ == '__main__':
    main()