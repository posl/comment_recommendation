def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(4 - (r == 1) - (r == h) - (c == 1) - (c == w))

if __name__ == '__main__':
    main()