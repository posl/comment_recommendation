def main():
    x, y = map(int, input().split())
    print(((y + 9) // 10) * 10 - x)

if __name__ == '__main__':
    main()