def main():
    x, y, z = map(int, input().split())
    if x < y:
        if y < z:
            print(-1)
        else:
            print(x + z)
    else:
        if z < y:
            print(-1)
        else:
            print(x + z)

if __name__ == '__main__':
    main()