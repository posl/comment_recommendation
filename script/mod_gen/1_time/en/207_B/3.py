def main():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print(-1)
        return
    count = 0
    while A > B * count:
        count += 1
    print(count)

if __name__ == '__main__':
    main()