def main():
    H, W = map(int, input().split())
    r, c = map(int, input().split())
    print((H-r+1)*(W-c+1))

if __name__ == '__main__':
    main()