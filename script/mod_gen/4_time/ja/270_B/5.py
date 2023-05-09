def main():
    x, y, z = map(int, input().split())
    if y < x:
        print(-1)
    else:
        print(z + (y - x) // 2)

if __name__ == '__main__':
    main()