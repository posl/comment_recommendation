def main():
    x, y, z = map(int, input().split())
    if x > y:
        print(x - y + z)
    else:
        print(-1)

if __name__ == '__main__':
    main()