def main():
    s, t, x = map(int, input().split())
    if s < t:
        print('Yes' if s <= x and t > x else 'No')
    else:
        print('Yes' if s <= x or t > x else 'No')

if __name__ == '__main__':
    main()