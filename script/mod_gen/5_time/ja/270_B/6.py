def main():
    x, y, z = map(int, input().split())
    if y > 0:
        print(-1)
    else:
        print(int((x-z)/(z-y)))

if __name__ == '__main__':
    main()