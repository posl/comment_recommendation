def main():
    a, b = map(int, input().split())
    print(max(a, b) * 2 - a - b)

if __name__ == '__main__':
    main()