def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print((H*W)-(H+W)+(R*C))

if __name__ == '__main__':
    main()