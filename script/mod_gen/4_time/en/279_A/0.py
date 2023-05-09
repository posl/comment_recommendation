def main():
    string = input()
    count = 0
    for i in range(len(string) - 1):
        if string[i] == 'v' and string[i + 1] == 'w':
            count += 1
    print(count)

if __name__ == '__main__':
    main()