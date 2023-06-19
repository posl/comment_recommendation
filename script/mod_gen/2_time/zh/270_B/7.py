def main():
    x,y,z = map(int, input().split())
    if x > y > z:
        print(x - z + y - z)
    elif x > z > y:
        print(x - y + z - y)
    elif y > x > z:
        print(y - z + x - z)
    elif y > z > x:
        print(y - x + z - x)
    elif z > x > y:
        print(z - y + x - y)
    elif z > y > x:
        print(z - x + y - x)
    else:
        print(-1)

if __name__ == '__main__':
    main()