def main():
    x, y = map(int, input().split())
    print("Yes" if abs(x-y) > 2 else "No")

if __name__ == '__main__':
    main()