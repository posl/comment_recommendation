def main():
    num = int(input())
    list = []
    list.append(num)
    while True:
        if num % 2 == 0:
            num = num / 2
            list.append(int(num))
        else:
            num = 3 * num + 1
            list.append(int(num))
        if list.count(num) == 2:
            break
    print(len(list))

if __name__ == '__main__':
    main()