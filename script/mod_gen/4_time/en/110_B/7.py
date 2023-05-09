def main():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a) < min(b) and max(a) < y and min(b) > x:
        print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()