def main():
    N = int(input())
    ans = 0
    while N > 1:
        for i in range(2, N+1):
            if N % i == 0:
                N //= i
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    main()