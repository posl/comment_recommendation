def main():
    n, r = map(int, input().split(' '))
    print(r + 100 * (10 - min(n, 10)))

if __name__ == '__main__':
    main()