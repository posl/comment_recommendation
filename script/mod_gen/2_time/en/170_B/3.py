def main():
    x, y = map(int, input().split())
    if x == 1 and y == 2:
        print('Yes')
        return
    for i in range(1, x):
        if 2 * i + 4 * (x - i) == y:
            print('Yes')
            return
    print('No')
    return
main()

if __name__ == '__main__':
    main()