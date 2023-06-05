def main():
    s = input()
    count = 0
    while int(s) != 0:
        if int(s) % 10 == 0:
            s = int(s) / 10
            count += 1
        else:
            s = int(s) - 1
            count += 1
    print(count)

if __name__ == '__main__':
    main()