def main():
    a, b = map(int, input().split())
    if a < b * 2:
        print(0)
    else:
        print(a - b * 2)
main()

if __name__ == '__main__':
    main()