def main():
    W = int(input())
    if W % 2 == 0:
        print(W // 2)
        for i in range(W // 2):
            print(2)
    else:
        print(W // 2 + 1)
        for i in range(W // 2):
            print(2)
        print(1)

if __name__ == '__main__':
    main()