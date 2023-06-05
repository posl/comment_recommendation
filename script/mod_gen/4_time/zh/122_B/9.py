def main():
    s = input()
    temp = 0
    max = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            temp += 1
            if max < temp:
                max = temp
        else:
            temp = 0
    print(max)

if __name__ == '__main__':
    main()