def main():
    x, y, z = map(int, input().split())
    if z < y < x:
        print(x + z - y)
    else:
        print(-1)

if __name__ == '__main__':
    main()