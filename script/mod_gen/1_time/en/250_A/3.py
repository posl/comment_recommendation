def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h-r)*(w-c))

if __name__ == '__main__':
    main()