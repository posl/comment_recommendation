def main():
    a, b = [int(x) for x in input().split()]
    x = (b - a) * (b - a + 1) // 2 - b
    print(x)

if __name__ == '__main__':
    main()