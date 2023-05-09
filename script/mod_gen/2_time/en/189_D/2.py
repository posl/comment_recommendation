def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 2 ** (N + 1) - 1
    print(ans)

if __name__ == '__main__':
    main()