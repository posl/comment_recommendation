def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    print(solve(N, P))

if __name__ == '__main__':
    main()