def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print((y - x) // 10)

if __name__ == '__main__':
    main()