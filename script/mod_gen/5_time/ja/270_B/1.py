def main():
    x, y, z = map(int, input().split())
    if x > 0:
        print(-1)
    else:
        print((y - x) // (z + 1) + 1)

if __name__ == '__main__':
    main()