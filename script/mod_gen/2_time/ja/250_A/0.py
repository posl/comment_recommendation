def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print((h-r+1)*(w-c+1))

if __name__ == '__main__':
    main()