def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += a[i] - 1
    print(ans)

if __name__ == '__main__':
    main()