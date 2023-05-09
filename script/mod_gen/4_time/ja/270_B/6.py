def main():
    # input
    x, y, z = map(int, input().split())
    # compute
    ans = 0
    if x < y:
        ans += y - x
    else:
        ans += x - y
    if y < z:
        ans += z - y
    else:
        ans += y - z
    # output
    if x < y < z:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()