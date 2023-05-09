def main():
    x,y,z = map(int, input().split())
    if x < y:
        if z < y:
            print(abs(x-z))
        else:
            print(abs(x-y)+abs(z-y))
    else:
        if z > y:
            print(abs(x-z))
        else:
            print(abs(x-y)+abs(z-y))

if __name__ == '__main__':
    main()