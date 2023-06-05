def main():
    str = input()
    count = 0
    for i in range(len(str)//2):
        if str[i] != str[-1-i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()