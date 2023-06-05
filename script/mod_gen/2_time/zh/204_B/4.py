def main():
    x, y = map(int, input().split())
    print((y - x + 3) % 3)

if __name__ == '__main__':
    main()