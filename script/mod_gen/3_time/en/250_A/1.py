def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    ans = 0
    if H != 1:
        ans += W
    if W != 1:
        ans += H
    if H != 1 and W != 1:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()