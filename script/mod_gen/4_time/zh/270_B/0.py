def main():
    x, y, z = map(int, input().split())
    if (x > 0 and y > 0 and z > 0) or (x < 0 and y < 0 and z < 0):
        print(-1)
    else:
        if x > 0:
            print(z + x - y)
        else:
            print(z + y - x)

if __name__ == '__main__':
    main()