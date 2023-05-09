def main():
    x, a, d, n = map(int, input().split())
    print(x + d * (n - 1) - a)
main()

if __name__ == '__main__':
    main()