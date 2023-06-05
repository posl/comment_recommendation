def main():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(-1)
    else:
        print(abs(x - z) + abs(z - y))

if __name__ == '__main__':
    main()