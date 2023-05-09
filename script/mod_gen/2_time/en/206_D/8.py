def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(N, A))

if __name__ == '__main__':
    main()