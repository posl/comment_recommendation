def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(0, C[i] - i)
        ans %= 1000000007
    print(ans)

if __name__ == '__main__':
    main()