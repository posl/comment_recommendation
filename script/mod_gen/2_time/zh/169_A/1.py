def main():
    a, b = map(int, input().split())
    if a >= 1 and a <= 100 and b >= 1 and b <= 100:
        print(a*b)

if __name__ == '__main__':
    main()