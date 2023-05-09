def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(max(a, c) - min(b, d), 0))

if __name__ == '__main__':
    main()