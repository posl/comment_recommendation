def main():
    n = int(input())
    x = 0
    while True:
        if x * x * x >= n:
            break
        x += 1
    while True:
        if x * x * x + x * x * x * x < n:
            break
        x -= 1
    print(x)

if __name__ == '__main__':
    main()