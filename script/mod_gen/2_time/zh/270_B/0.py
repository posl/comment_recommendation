def main():
    x,y,z = map(int, input().split())
    if y > z:
        print(-1)
    else:
        print((x*y)//(z-y))

if __name__ == '__main__':
    main()