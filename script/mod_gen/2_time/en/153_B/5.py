def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= max(a):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()