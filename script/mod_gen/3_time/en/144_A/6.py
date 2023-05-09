def main():
    a, b = map(int, input().split())
    print(a * b if a <= 9 and b <= 9 else -1)

if __name__ == '__main__':
    main()