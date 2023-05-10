def main():
    H = int(input())
    count = 0
    while H > 0:
        H = H // 2
        count += 1
    print(2 ** count - 1)

if __name__ == '__main__':
    main()