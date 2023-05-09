def main():
    N = int(input())
    k = int(N ** 0.5)
    ans = N - k - 1
    for i in range(2, k + 1):
        j = 2
        while i ** j <= N:
            ans -= 1
            j += 1
    print(ans)

if __name__ == '__main__':
    main()