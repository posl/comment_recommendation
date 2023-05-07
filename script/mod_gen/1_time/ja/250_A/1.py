def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    if H == 1 and W == 1:
        print(0)
    elif H == 1 and W > 1:
        print(2)
    elif H > 1 and W == 1:
        print(1)
    else:
        print(4)

if __name__ == '__main__':
    main()