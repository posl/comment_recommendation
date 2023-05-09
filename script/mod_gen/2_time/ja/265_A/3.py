def main():
    x, y, n = map(int, input().split())
    cost = 0
    while n > 0:
        if n >= 3:
            n -= 3
            cost += y
        else:
            n -= 1
            cost += x
    print(cost)

if __name__ == '__main__':
    main()