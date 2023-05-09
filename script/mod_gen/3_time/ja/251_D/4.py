def main():
    W = int(input())
    if W <= 2:
        print(1)
        print(W)
    elif W <= 4:
        print(2)
        print(1, W-1)
    else:
        print(3)
        if W % 2 == 0:
            print(W//2, W//2)
        else:
            print(W//2, W//2+1)

if __name__ == '__main__':
    main()