def main():
    x, y, z = list(map(int, input().split()))
    if x < y < z or x > y > z:
        print(-1)
    else:
        print(abs(x-z) + abs(x-y))

if __name__ == '__main__':
    main()