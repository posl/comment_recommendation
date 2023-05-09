def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(max(a, b) - min(c, d), max(c, d) - min(a, b)))

if __name__ == '__main__':
    main()