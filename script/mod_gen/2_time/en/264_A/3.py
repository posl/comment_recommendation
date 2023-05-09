def main():
    l, r = map(int, input().split())
    print(''.join(list('atcoder')[l-1:r]))

if __name__ == '__main__':
    main()