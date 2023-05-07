def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max([b - c, b - d, a - c, a - d]))

if __name__ == '__main__':
    main()