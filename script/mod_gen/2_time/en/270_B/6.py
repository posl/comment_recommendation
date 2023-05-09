def main():
    x, y, z = map(int, input().split())
    if x < y:
        if z > y:
            print(-1)
        else:
            print(x-y)
    else:
        if z > x:
            print(-1)
        else:
            print(y-x)

if __name__ == '__main__':
    main()