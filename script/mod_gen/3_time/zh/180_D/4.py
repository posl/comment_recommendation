def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while True:
        if x * a < x + b and x * a < y:
            x *= a
            exp += 1
        else:
            exp += (y - x - 1) // b
            break
    print(exp)

if __name__ == '__main__':
    main()