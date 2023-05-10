def main():
    s, t, x = map(int, input().split())
    print("Yes" if s <= x <= t else "No")

if __name__ == '__main__':
    main()