def main():
    h, w, r, c = map(int, input().split())
    print((r > 1) + (r < h) + (c > 1) + (c < w))

if __name__ == '__main__':
    main()