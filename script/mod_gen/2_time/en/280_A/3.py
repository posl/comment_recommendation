def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        ans += S[i].count('#')
    print(ans)

if __name__ == '__main__':
    main()