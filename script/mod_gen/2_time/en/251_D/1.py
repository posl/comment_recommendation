def main():
    W = int(input())
    if W % 2 == 0:
        print(W//2)
        print(" ".join([str(i) for i in range(1,W//2+1)]))
    else:
        print(W//2)
        print(" ".join([str(i) for i in range(1,W//2+2)]))
main()

if __name__ == '__main__':
    main()