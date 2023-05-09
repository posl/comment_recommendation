def main():
    # data load
    x, y, z = map(int, input().split())
    # calc
    if y > x:
        print(-1)
    else:
        print((x-y) // (z+y))

if __name__ == '__main__':
    main()