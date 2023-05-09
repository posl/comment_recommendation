def main():
    x, y, z = map(int, input().split())
    if y < z < x:
        print('{}'.format(x - y + z))
    else:
        print('-1')

if __name__ == '__main__':
    main()