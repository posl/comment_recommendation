def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if H[i] >= H[i - 1]:
            ans = max(ans, H[i])
    print(ans)

if __name__ == '__main__':
    main()