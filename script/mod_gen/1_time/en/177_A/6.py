def main():
    d, t, s = map(int, input().split())
    if s * t >= d:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()