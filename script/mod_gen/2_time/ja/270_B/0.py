def main():
    x, y, z = map(int, input().split())
    if z > 0:
        if x > y:
            print(x - y)
        else:
            print(-1)
    else:
        if x < y:
            print(y - x)
        else:
            print(-1)

if __name__ == '__main__':
    main()