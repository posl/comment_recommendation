def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 1
    for i in range(1, N):
        if H[i-1] < H[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()