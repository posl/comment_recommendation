def main():
    s = input()
    #print(s)
    max = 0
    count = 0
    for i in range(3):
        if s[i] == "R":
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
main()

if __name__ == '__main__':
    main()