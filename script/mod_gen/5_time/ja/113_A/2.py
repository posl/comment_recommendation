def main():
    x, y = map(int, input().split())
    if y % 2 == 0:
        print(x * (y // 2))
    else:
        print(-1)

if __name__ == '__main__':
    main()