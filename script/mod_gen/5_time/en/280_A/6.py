def main():
    # input
    H, W = map(int, input().split())
    # solve
    ans = 0
    for _ in range(H):
        ans += input().count("#")
    # output
    print(ans)

if __name__ == '__main__':
    main()