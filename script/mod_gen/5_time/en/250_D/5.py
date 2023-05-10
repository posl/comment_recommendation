def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N ** (1/3)) + 1):
        if N % i == 0:
            m = N // i
            for j in range(1, int(m ** (1/2)) + 1):
                if m % j == 0 and j < m // j:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()