def main():
    #input
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    #output
    print((H-h)*(W-w))

if __name__ == '__main__':
    main()