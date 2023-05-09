def main():
    a, b = map(int, input().split())
    print(b - a + 1 if b > a else 0)
main()

if __name__ == '__main__':
    main()