def main():
    x, y, z = map(int, input().split())
    if x > y and y > z:
        print('{}'.format(x - z))
    else:
        print('-1')

if __name__ == '__main__':
    main()