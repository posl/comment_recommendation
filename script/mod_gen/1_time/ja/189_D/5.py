def main():
    N = int(input())
    S = [input() for i in range(N)]
    ans = 2**(N-1)
    print(ans)

if __name__ == '__main__':
    main()