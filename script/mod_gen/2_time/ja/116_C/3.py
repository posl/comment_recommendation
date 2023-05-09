def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += h[i]
    print(ans)

if __name__ == '__main__':
    main()