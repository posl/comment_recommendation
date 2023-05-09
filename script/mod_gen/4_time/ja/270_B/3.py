def main():
    x, y, z = map(int, input().split())
    a = x - z
    b = x + z
    if y < a or b < y:
        print(-1)
    else:
        print(a)

if __name__ == '__main__':
    main()