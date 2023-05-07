def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(4 - (R==1) - (R==H) - (C==1) - (C==W))

if __name__ == '__main__':
    main()