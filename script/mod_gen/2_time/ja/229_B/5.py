def main():
    a, b = map(int, input().split())
    print("Easy" if a + b < 10 ** 19 else "Hard")

if __name__ == '__main__':
    main()