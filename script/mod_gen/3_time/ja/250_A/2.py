def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    count = 0
    if R > 1:
        count += 1
    if R < H:
        count += 1
    if C > 1:
        count += 1
    if C < W:
        count += 1
    print(count)

if __name__ == '__main__':
    main()