def main():
    a, b = map(int, input().split())
    if a == 0:
        print('银')
    elif b == 0:
        print('黄金')
    else:
        print('合金')

if __name__ == '__main__':
    main()