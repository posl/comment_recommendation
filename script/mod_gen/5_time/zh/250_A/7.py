def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(H*W - (H*C+W*R-C*R)*2 + 4*R*C - 3*R - 3*C + 4)

if __name__ == '__main__':
    main()