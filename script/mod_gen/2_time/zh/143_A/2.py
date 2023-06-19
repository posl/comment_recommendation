def main():
    a, b = map(int, input().split())
    print(max(a - b * 2, 0))

if __name__ == '__main__':
    main()