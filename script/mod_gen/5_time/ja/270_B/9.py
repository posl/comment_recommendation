def main():
    x, y, z = map(int, input().split())
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        print(-1)
    else:
        print(abs(x - y) // z)

if __name__ == '__main__':
    main()