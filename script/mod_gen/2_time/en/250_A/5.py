def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print(2*(H-1) + 2*(W-1) - (R==H) - (C==W))
main()

if __name__ == '__main__':
    main()