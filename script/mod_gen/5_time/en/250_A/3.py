def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H-R)*(W-C))

if __name__ == '__main__':
    main()