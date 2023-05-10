def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            if (y - x) % b == 0:
                exp += (y - x) // b - 1
                break
            else:
                exp += (y - x) // b
                break
    print(exp)

if __name__ == '__main__':
    main()