def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        else:
            y += 1
    return

if __name__ == '__main__':
    main()