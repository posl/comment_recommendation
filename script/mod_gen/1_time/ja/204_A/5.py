def main():
    x, y = map(int, input().split())
    print((x + 1) % 3) if x != y else print(x)

if __name__ == '__main__':
    main()