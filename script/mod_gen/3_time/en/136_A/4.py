def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if c - (a - b) > 0 else 0)

if __name__ == '__main__':
    main()