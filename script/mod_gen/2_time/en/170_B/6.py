def main():
    x, y = map(int, input().split())
    if x*2 == y or x*4 == y or (x*2 + x*4) == y:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()