def main():
    a, b = map(int, input().split())
    print("Yes" if (a * b) % 2 == 1 else "No")
    return

if __name__ == '__main__':
    main()