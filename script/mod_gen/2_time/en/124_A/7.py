def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print(a * 2 - 1 if a != b else a * 2)
main()

if __name__ == '__main__':
    main()