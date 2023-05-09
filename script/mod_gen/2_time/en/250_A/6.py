def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(2 * (h + w) - 4 - (r == h) - (c == w))
main()

if __name__ == '__main__':
    main()