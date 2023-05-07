def main():
    W = int(input())
    if W <= 2:
        print(2)
        print(1,1)
    else:
        print(W)
        for i in range(1,W):
            print(i,i+1)
    return

if __name__ == '__main__':
    main()