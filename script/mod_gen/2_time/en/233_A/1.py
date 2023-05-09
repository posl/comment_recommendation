def main():
    x, y = map(int, input().split())
    print(max(0, y - x))

if __name__ == '__main__':
    main()