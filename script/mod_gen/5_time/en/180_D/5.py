def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y and (a-1)*x < b:
        x *= a
        exp += 1
    exp += (y - 1 - x) // b
    print(exp)

if __name__ == '__main__':
    main()