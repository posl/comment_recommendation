def main():
    x, y = map(int, input().split())
    print(0 if x >= y else y - x)

if __name__ == '__main__':
    main()