def main():
    count = 0
    for i in range(9):
        s = input()
        for j in range(9):
            if s[j] == '#':
                count += 1
    print(count)

if __name__ == '__main__':
    main()