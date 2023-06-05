def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(z + x - y)
    else:
        print(-1)

if __name__ == '__main__':
    main()