def main():
    str = input()
    max = 0
    count = 0
    for i in range(len(str)):
        if str[i] == "A" or str[i] == "C" or str[i] == "G" or str[i] == "T":
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

if __name__ == '__main__':
    main()