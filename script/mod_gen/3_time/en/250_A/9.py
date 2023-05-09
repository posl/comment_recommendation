def main():
    #input
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    #output
    print(2 * (H + W) - 4)

if __name__ == '__main__':
    main()