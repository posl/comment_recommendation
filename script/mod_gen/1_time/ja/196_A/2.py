def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a - d, b - c))

if __name__ == '__main__':
    main()