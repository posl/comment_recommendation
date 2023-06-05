def main():
    H = input()
    H = int(H)
    count = 0
    while 1:
        if H == 1:
            count += 1
            break
        else:
            H = int(H / 2)
            count += 1
    print(count)

if __name__ == '__main__':
    main()