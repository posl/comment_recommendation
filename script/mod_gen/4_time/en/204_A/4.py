def main():
    x, y = map(int, input().split())
    z = 0
    if x == y:
        z = x
    else:
        z = 3 - (x + y)
    print(z)
main()

if __name__ == '__main__':
    main()