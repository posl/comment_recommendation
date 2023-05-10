def main():
    a, b = map(int, input().split())
    print(a - b * 2 if a >= b * 2 else 0)

if __name__ == '__main__':
    main()