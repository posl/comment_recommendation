def main():
    H, W = map(int, input().split())
    ans = 0
    for i in range(H):
        ans += input().count('#')
    print(ans)

if __name__ == '__main__':
    main()