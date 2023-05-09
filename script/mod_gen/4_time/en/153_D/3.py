def main():
    H = int(input())
    counter = 0
    while H > 0:
        H = H // 2
        counter = counter + 1
    print(2**counter - 1)

if __name__ == '__main__':
    main()