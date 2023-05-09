def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        j = 2
        while i ** j <= N:
            ans += 1
            j += 1
    print(N - ans)
main()

if __name__ == '__main__':
    main()