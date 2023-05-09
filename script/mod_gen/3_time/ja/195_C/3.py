def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += (N // (10 ** (3 * i))) * (3 * i)
    ans += (N % (10 ** 3))
    print(ans)

if __name__ == '__main__':
    main()