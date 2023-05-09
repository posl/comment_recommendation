def main():
    a, b = map(int, input().split())
    print(max(b - a + 1, 0))

if __name__ == '__main__':
    main()