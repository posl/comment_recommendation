def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N - i - 1) * (i + 1)
    print(ans)

if __name__ == '__main__':
    main()