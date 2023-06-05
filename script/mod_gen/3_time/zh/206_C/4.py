def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, nums))

if __name__ == '__main__':
    main()