def main():
    a, b, c = map(int, input().split())
    print("Yes" if a < b < c or c < b < a else "No")

if __name__ == '__main__':
    main()