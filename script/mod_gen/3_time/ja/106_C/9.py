def main():
    str = input()
    num = int(input())
    if num <= len(str):
        print(str[num-1])
    else:
        for i in range(0, num-len(str)):
            str = str.replace("2", "22")
            str = str.replace("3", "333")
            str = str.replace("4", "4444")
            str = str.replace("5", "55555")
            str = str.replace("6", "666666")
            str = str.replace("7", "7777777")
            str = str.replace("8", "88888888")
            str = str.replace("9", "999999999")
        print(str[num-1])

if __name__ == '__main__':
    main()