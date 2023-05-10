def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            exp += (y - x - 1) // b
            break
    print(exp)

if __name__ == '__main__':
    main()