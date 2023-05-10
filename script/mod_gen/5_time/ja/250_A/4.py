def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    ans = 0
    if R != 1:
        ans += 1
    if R != H:
        ans += 1
    if C != 1:
        ans += 1
    if C != W:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()