def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h-r) * (w-c) + (r-1) * (w-c) + (h-r) * (c-1) + (r-1) * (c-1) + 1)

if __name__ == '__main__':
    main()