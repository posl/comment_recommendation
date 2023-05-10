def main():
    x, y, z = map(int, input().split())
    if y > x:
        print(-1)
    else:
        print((x-z)//(y+z))

if __name__ == '__main__':
    main()